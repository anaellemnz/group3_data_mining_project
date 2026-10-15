from pathlib import Path
import os

attributes_subset_for_models = [
    "DUPERSID",
    "TOTEXP23",
    "PHYEXE53",
    "OFTSMK53",
    "AGE23X",
    "SEX",
    "INSCOV23",
    "POVCAT23",
    "PERWT23F",
]

ROW_ID = "DUPERSID"


WEIGHT = "PERWT23F"

EXPENDITURE = "TOTEXP23"


BASELINE_FEATURES = ["AGE23X", "SEX", "INSCOV23"]
EXPANDED_FEATURES = BASELINE_FEATURES + ["PHYEXE53", "OFTSMK53"]
OPTIONAL_FEATURES = ["POVCAT23"]


CATEGORICAL_FEATURES = ["SEX", "INSCOV23", "PHYEXE53", "OFTSMK53", "POVCAT23"]


TARGET = "TOTEXP23_binary"
TARGET_PERCENTILE = 0.75


MISSING_CODES = [-1, -7, -8, -15]

SEED = 42

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


############################################# Data file paths
RAW_DATA = os.path.join(PROJECT_ROOT, "data", "raw", "h251.dta")

PREPARED_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "prepared")

COLUMN_SUBSET_FILE = os.path.join(PREPARED_DATA_DIR, "data_columns_subset.dta")

CLEANED_DATA_FILE = os.path.join(PREPARED_DATA_DIR, "data_cleaned.dta")


SPLITS_DIR = os.path.join(PROJECT_ROOT, "data", "splits")

############################################# filepaths for train, validation, and test splits
TRAIN_FILE = os.path.join(SPLITS_DIR, "train.dta")

VALIDATION_FILE = os.path.join(SPLITS_DIR, "validation.dta")

TEST_FILE = os.path.join(SPLITS_DIR, "test.dta")

############################### filepaths for results: models, predictions, tables and figures
MODELS_DIR = os.path.join(PROJECT_ROOT, "results", "models")
PREDICTIONS_DIR = os.path.join(PROJECT_ROOT, "results", "predictions")
TABLES_DIR = os.path.join(PROJECT_ROOT, "results", "tables")
FIGURES_DIR = os.path.join(PROJECT_ROOT, "results", "figures")

################################ Also need the prediction column name for the test set predictions
PREDICTION_COLUMN = "y_pred"