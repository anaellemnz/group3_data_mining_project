import pandas as pd

df = pd.read_stata(
    "../data/data_columns_subset.dta",
    convert_categoricals=False,
)

print("Column datatypes:")
print(df.dtypes)

print("\nActual missing values:")
print(df.isna().sum())

for column in df.columns:
    print(f"\n--- {column} ---")
    print(df[column].value_counts(dropna=False).sort_index())