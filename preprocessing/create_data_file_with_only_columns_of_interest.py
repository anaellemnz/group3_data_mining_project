import pandas as pd

df = pd.read_stata("../data/h251.dta", convert_categoricals=False)

# Take only these columns from the original dataset
attributes_subset_for_model = [
    "TOTEXP23",
    "PHYEXE53",
    "OFTSMK53",
    "AGE23X",
    "SEX",
    "INSCOV23",
    "POVCAT23",
    "PERWT23F",
]

sub_df = df[attributes_subset_for_model].copy()

for att in attributes_subset_for_model:
    print(att)

# Check that we have those columns we wanted
print("subsetted attributes df columns (includes both models features): ", sub_df.columns)

# Check for missing values (no missing values according to documentation)
print("sub_df.isna().sum() (Doesn't tell us about codes used by the dataset for missing values, need to inspect that separately): ")
print( sub_df.isna().sum() )

sub_df.to_stata("../data/data_columns_subset.dta", write_index=False)