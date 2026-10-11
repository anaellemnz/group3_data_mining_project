import pandas as pd

df = pd.read_stata("h251.dta")

print(df.head())

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

for att in attributes_subset_for_model:
    print(att)

sub_df = df[attributes_subset_for_model]

print("subsetted attributes df columns (includes both models features): ", sub_df.columns)

print("Missing values per column: ")
print( sub_df.isna().sum() )

sub_df.to_stata("data_column_subset.dta", write_index = False)
