import os
import pandas as pd
from src.config import PREPARED_DATA_DIR

col_subset_data = os.path.join(PREPARED_DATA_DIR, "data_columns_subset.dta")

df = pd.read_stata(
    col_subset_data,
    convert_categoricals=False,
)

print("Column datatypes:")
print(df.dtypes)

for column in df.columns:
    print(f"\n--- {column} ---")
    print(df[column].value_counts(dropna=False).sort_index())