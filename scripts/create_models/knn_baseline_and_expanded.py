import os
import pandas as pd

from src.config import (
    TRAIN_FILE,
    VALIDATION_FILE,
    TEST_FILE,
    MODELS_DIR,
    PREDICTIONS_DIR,
    TABLES_DIR,
    FIGURES_DIR,
)

# Load datasets (same files, same splits as the logistic regression).
train = pd.read_stata(TRAIN_FILE, convert_categoricals=False)
validation = pd.read_stata(VALIDATION_FILE, convert_categoricals=False)
test = pd.read_stata(TEST_FILE, convert_categoricals=False)

MODEL_NAME = "knn"

# Model paths.
baseline_model_path = os.path.join(MODELS_DIR, f"{MODEL_NAME}_baseline.joblib")
expanded_model_path = os.path.join(MODELS_DIR, f"{MODEL_NAME}_expanded.joblib")

# Prediction paths.
baseline_test_predictions_path = os.path.join(
    PREDICTIONS_DIR, f"{MODEL_NAME}_baseline_test.csv"
)
expanded_test_predictions_path = os.path.join(
    PREDICTIONS_DIR, f"{MODEL_NAME}_expanded_test.csv"
)

# Results table paths.
validation_results_path = os.path.join(
    TABLES_DIR, f"{MODEL_NAME}_validation_results.csv"
)
test_metrics_path = os.path.join(
    TABLES_DIR, f"{MODEL_NAME}_test_metrics.csv"
)

# Figure paths.
baseline_confusion_matrix_path = os.path.join(
    FIGURES_DIR, f"{MODEL_NAME}_baseline_confusion_matrix.png"
)
expanded_confusion_matrix_path = os.path.join(
    FIGURES_DIR, f"{MODEL_NAME}_expanded_confusion_matrix.png"
)

# ######################################## Model training and evaluation ########################################
import joblib
import matplotlib.pyplot as plt
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    ConfusionMatrixDisplay,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import (
    BASELINE_FEATURES,
    EXPANDED_FEATURES,
    CATEGORICAL_FEATURES,
    TARGET,
    ROW_ID,
    PREDICTION_COLUMN,
)

for directory in [MODELS_DIR, PREDICTIONS_DIR, TABLES_DIR, FIGURES_DIR]:
    os.makedirs(directory, exist_ok=True)

feature_sets = {
    "baseline": BASELINE_FEATURES,
    "expanded": EXPANDED_FEATURES,
}

model_paths = {
    "baseline": baseline_model_path,
    "expanded": expanded_model_path,
}

prediction_paths = {
    "baseline": baseline_test_predictions_path,
    "expanded": expanded_test_predictions_path,
}

figure_paths = {
    "baseline": baseline_confusion_matrix_path,
    "expanded": expanded_confusion_matrix_path,
}

# KNN search space.
K_VALUES = list(range(5, 102, 4))          # 5, 9, ..., 101
WEIGHT_OPTIONS = ["uniform", "distance"]
# KNN has no class_weight="balanced" like his logistic regression, so we tune
# the decision threshold on validation F1 instead. This is the equivalent
# way to handle the rare high-expenditure class.
THRESHOLDS = np.linspace(0.05, 0.95, 91)


def create_pipeline(features, k, weights):
    categorical = [
        column for column in features
        if column in CATEGORICAL_FEATURES
    ]
    numeric = [
        column for column in features
        if column not in CATEGORICAL_FEATURES
    ]

    # Same preprocessing as the logistic regression pipeline.
    preprocessing = ColumnTransformer([
        ("numeric", StandardScaler(), numeric),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical,
        ),
    ])

    return Pipeline([
        ("preprocessing", preprocessing),
        (
            "classifier",
            KNeighborsClassifier(n_neighbors=k, weights=weights),
        ),
    ])


def calculate_metrics(y_true, y_pred, y_score=None):
    # First four metrics are identical to the logistic regression script.
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true, y_pred, pos_label=1, zero_division=0
        ),
        "recall": recall_score(
            y_true, y_pred, pos_label=1, zero_division=0
        ),
        "f1": f1_score(
            y_true, y_pred, pos_label=1, zero_division=0
        ),
    }
    # Extra, threshold-free metric (useful for baseline vs. expanded).
    if y_score is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_score)
    return metrics


def save_predictions(data, predictions, path):
    pd.DataFrame({
        ROW_ID: data[ROW_ID].to_numpy(),
        TARGET: data[TARGET].to_numpy(),
        PREDICTION_COLUMN: predictions,
    }).to_csv(path, index=False)


# Check shared data.
for data in [train, validation, test]:
    assert data[ROW_ID].notna().all()
    assert data[ROW_ID].is_unique
    assert data[TARGET].isin([0, 1]).all()
    assert not data[EXPANDED_FEATURES].isna().any().any()

train_ids = set(train[ROW_ID])
validation_ids = set(validation[ROW_ID])
test_ids = set(test[ROW_ID])

assert train_ids.isdisjoint(validation_ids)
assert train_ids.isdisjoint(test_ids)
assert validation_ids.isdisjoint(test_ids)


# Train and validate.
validation_results = []
selected_params = {}

for name, features in feature_sets.items():
    best_f1 = -1
    best_row = None
    best_scores = None

    for weights in WEIGHT_OPTIONS:
        for k in K_VALUES:
            pipeline = create_pipeline(features, k, weights)
            pipeline.fit(train[features], train[TARGET])

            # Fit once per (k, weights), then sweep thresholds cheaply.
            scores = pipeline.predict_proba(validation[features])[:, 1]

            best_threshold_f1 = -1
            best_threshold = None
            for threshold in THRESHOLDS:
                predictions = (scores >= threshold).astype(int)
                f1 = f1_score(
                    validation[TARGET], predictions,
                    pos_label=1, zero_division=0,
                )
                if f1 > best_threshold_f1:
                    best_threshold_f1 = f1
                    best_threshold = threshold

            predictions = (scores >= best_threshold).astype(int)
            metrics = calculate_metrics(
                validation[TARGET], predictions, scores
            )

            # One row per (k, weights), at its best threshold.
            result = {
                "model": MODEL_NAME,
                "feature_set": name,
                "k": k,
                "weights": weights,
                "threshold": best_threshold,
                **metrics,
                "selected": False,
            }
            validation_results.append(result)

            if metrics["f1"] > best_f1:
                best_f1 = metrics["f1"]
                selected_params[name] = {
                    "k": k,
                    "weights": weights,
                    "threshold": best_threshold,
                }
                best_row = result
                best_scores = scores

    best_row["selected"] = True

    # These predictions come from a model fitted only on training data.
    validation_predictions = (
        best_scores >= selected_params[name]["threshold"]
    ).astype(int)
    print(pd.Series(validation_predictions).value_counts())

    save_predictions(
        validation,
        validation_predictions,
        os.path.join(
            PREDICTIONS_DIR,
            f"{MODEL_NAME}_{name}_validation.csv",
        ),
    )
    print(validation[TARGET].value_counts(normalize=True))

    print(
        f"{name}: selected {selected_params[name]}, "
        f"validation F1={best_f1:.4f}"
    )

validation_df = pd.DataFrame(validation_results)
validation_df.to_csv(validation_results_path, index=False)

# Validation metrics vs. k (best threshold at each k, best weighting option).
fig, axes = plt.subplots(2, 2, figsize=(10, 7))

for ax, metric in zip(
    axes.flat, ["accuracy", "precision", "recall", "f1"]
):
    for name in feature_sets:
        subset = validation_df[validation_df["feature_set"] == name]
        # Keep the best-F1 weighting option for each k.
        subset = (
            subset.sort_values("f1", ascending=False)
            .drop_duplicates("k")
            .sort_values("k")
        )

        ax.plot(
            subset["k"],
            subset[metric],
            marker="o",
            label=name.capitalize(),
        )

    ax.set_xlabel("k (number of neighbors)")
    ax.set_ylabel(metric.capitalize())
    ax.set_ylim(0, 1)
    ax.set_title(f"Validation {metric}")
    ax.grid(True, alpha=0.3)
    ax.legend()

fig.suptitle("KNN: Validation Metrics vs. k")
fig.tight_layout()

fig.savefig(
    os.path.join(FIGURES_DIR, f"{MODEL_NAME}_validation_metrics_vs_k.png"),
    dpi=300,
    bbox_inches="tight",
)

plt.show()
plt.close(fig)

# Set True only when all model and ensemble choices are finalized.
RUN_FINAL_TEST = False

if RUN_FINAL_TEST:
    train_validation = pd.concat(
        [train, validation], ignore_index=True
    )
    test_results = []

    for name, features in feature_sets.items():
        params = selected_params[name]
        final_pipeline = create_pipeline(
            features, params["k"], params["weights"]
        )
        final_pipeline.fit(
            train_validation[features],
            train_validation[TARGET],
        )

        joblib.dump(
            {"pipeline": final_pipeline, "threshold": params["threshold"]},
            model_paths[name],
        )

        scores = final_pipeline.predict_proba(test[features])[:, 1]
        predictions = (scores >= params["threshold"]).astype(int)
        metrics = calculate_metrics(test[TARGET], predictions, scores)

        save_predictions(test, predictions, prediction_paths[name])

        test_results.append({
            "model": MODEL_NAME,
            "feature_set": name,
            "k": params["k"],
            "weights": params["weights"],
            "threshold": params["threshold"],
            **metrics,
        })

        fig, ax = plt.subplots(figsize=(5, 4))
        ConfusionMatrixDisplay.from_predictions(
            test[TARGET],
            predictions,
            labels=[0, 1],
            display_labels=["Lower expenditure", "High expenditure"],
            cmap="Blues",
            colorbar=False,
            ax=ax,
        )
        ax.set_title(f"{MODEL_NAME}: {name}")
        fig.tight_layout()
        fig.savefig(figure_paths[name], dpi=300)
        plt.close(fig)

        print(f"\n{name} test metrics:")
        print(metrics)

    pd.DataFrame(test_results).to_csv(
        test_metrics_path, index=False
    )
