import os
import pandas as pd
from src.config import RAW_DATA, attributes_subset_for_models, PREPARED_DATA_DIR

# We want to get the attributes we'll use for our models. We want to include DUPERSID 
# to keep track of each observation

print('\nRaw data absolute path:\n', RAW_DATA)

df = pd.read_stata(RAW_DATA, convert_categoricals=False)

sub_df = df[attributes_subset_for_models].copy()

print("\nExpected list of chosen attributes:")
for att in attributes_subset_for_models:
    print(att)

# # Check that we have those columns we wanted
print("\nActual list of columns in the subsetted dataframe: ", sub_df.columns)

# Check for missing values (no null values, but codes used for missing values)
print("\nsub_df.isna().sum() (Doesn't tell us about codes used by the dataset for missing values, need to inspect that separately): ")
print( sub_df.isna().sum() )

data_columns_subset_path = os.path.join(PREPARED_DATA_DIR, "data_columns_subset.dta")

print('\nSaving the subsetted dataframe to a new Stata file\n', data_columns_subset_path)
sub_df.to_stata(data_columns_subset_path, write_index=False)