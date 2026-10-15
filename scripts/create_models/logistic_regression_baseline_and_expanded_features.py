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

# Load datasets.
train = pd.read_stata(TRAIN_FILE, convert_categoricals=False)
validation = pd.read_stata(VALIDATION_FILE, convert_categoricals=False)
test = pd.read_stata(TEST_FILE, convert_categoricals=False)

# Change to "knn" or "decision_tree" for your algorithm.
MODEL_NAME = "logistic"

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