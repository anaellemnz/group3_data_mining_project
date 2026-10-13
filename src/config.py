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

from pathlib import Path
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

RAW_DATA = os.path.join(PROJECT_ROOT, "data", "raw", "h251.dta")

PREPARED_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "prepared")


SPLITS_DIR = os.path.join(PROJECT_ROOT, "data", "splits")

TRAIN_FILE = os.path.join(SPLITS_DIR, "train.dta")

VALIDATION_FILE = os.path.join(SPLITS_DIR, "validation.dta")

TEST_FILE = os.path.join(SPLITS_DIR, "test.dta")