import pandas as pd

from src.config import (
    CLEANED_DATA_FILE,
    COLUMN_SUBSET_FILE,
    EXPANDED_FEATURES,
    EXPENDITURE,
    MISSING_CODES,
    OPTIONAL_FEATURES,
    TARGET,
    TARGET_PERCENTILE,
    WEIGHT,
)

df = pd.read_stata(COLUMN_SUBSET_FILE, convert_categoricals=False)
print(f"Adults in column subset: {len(df)}")


columns_to_check = EXPANDED_FEATURES + OPTIONAL_FEATURES + [EXPENDITURE]
print("\nRows with a missing-response code, per column:")
for col in columns_to_check:
    n_missing = df[col].isin(MISSING_CODES).sum()
    print(f"  {col:10s} {n_missing}")

has_missing_code = df[columns_to_check].isin(MISSING_CODES).any(axis=1)
df = df.loc[~has_missing_code].copy()
print(f"Dropped {has_missing_code.sum()} rows -> {len(df)} remaining")


zero_weight = df[WEIGHT] == 0
df = df.loc[~zero_weight].copy()
print(f"\nDropped {zero_weight.sum()} rows with {WEIGHT} = 0 -> {len(df)} remaining")


cutoff = df[EXPENDITURE].quantile(TARGET_PERCENTILE)
df[TARGET] = (df[EXPENDITURE] > cutoff).astype("int8")

print(f"\n{int(TARGET_PERCENTILE * 100)}th-percentile cutoff (unweighted, cleaned adults): ${cutoff:,.2f}")
print(f"Observations exactly at the cutoff (assigned 0): {(df[EXPENDITURE] == cutoff).sum()}")
print("Class counts:")
print(df[TARGET].value_counts().sort_index().to_string())
print("Class proportions:")
print(df[TARGET].value_counts(normalize=True).sort_index().round(4).to_string())

df = df.drop(columns=[EXPENDITURE])


assert df["DUPERSID"].is_unique, "Duplicate person IDs"
assert not df[EXPANDED_FEATURES + OPTIONAL_FEATURES].isin(MISSING_CODES).any().any()
assert (df[WEIGHT] > 0).all()

df.to_stata(CLEANED_DATA_FILE, write_index=False, version=118)
print(f"\nSaved {len(df)} rows x {df.shape[1]} columns to:\n  {CLEANED_DATA_FILE}")
print("Columns:", list(df.columns))