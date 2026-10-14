
import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import (
    CLEANED_DATA_FILE,
    ROW_ID,
    SEED,
    SPLITS_DIR,
    TARGET,
    TEST_FILE,
    TRAIN_FILE,
    VALIDATION_FILE,
)

df = pd.read_stata(CLEANED_DATA_FILE, convert_categoricals=False)
print(f"Cleaned rows: {len(df)}")


train, remaining = train_test_split(
    df,
    test_size=0.40,
    stratify=df[TARGET],
    random_state=SEED,
)


validation, test = train_test_split(
    remaining,
    test_size=0.50,
    stratify=remaining[TARGET],
    random_state=SEED,
)


train_ids, val_ids, test_ids = set(train[ROW_ID]), set(validation[ROW_ID]), set(test[ROW_ID])
assert not (train_ids & val_ids), "train and validation overlap"
assert not (train_ids & test_ids), "train and test overlap"
assert not (val_ids & test_ids), "validation and test overlap"
assert len(train_ids | val_ids | test_ids) == len(df), "rows lost during splitting"
print("Checked: no overlap between splits, all rows assigned.")

os.makedirs(SPLITS_DIR, exist_ok=True)

for name, split, path in [
    ("train", train, TRAIN_FILE),
    ("validation", validation, VALIDATION_FILE),
    ("test", test, TEST_FILE),
]:
    split.to_stata(path, write_index=False, version=118)
    share = split[TARGET].mean()
    print(f"{name:10s} {len(split):5d} rows  ({len(split) / len(df):.0%})  "
          f"positive class: {share:.2%}  -> {path}")