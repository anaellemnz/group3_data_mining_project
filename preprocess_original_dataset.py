import pandas as pd

df = pd.read_stata("h251.dta", convert_categoricals=False)

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
print("Missing values per column(before transforming TOTEXP23): ")
print( sub_df.isna().sum() )

# Make the new binary variable
print("Transforming TOTEXP23 into TOTEXP23_binary.")
cutoff = sub_df["TOTEXP23"].quantile(0.75)

# 1 = top 25%; 0 = lower 75%.
sub_df["TOTEXP23_binary"] = (
    sub_df["TOTEXP23"] > cutoff
).astype("int8")

# Drop the original column because we don't want to include it in the model by accident
sub_df = sub_df.drop(columns=["TOTEXP23"])

# Check the class proportions (should be about 75% and 25%)
print("75th-percentile expenditure cutoff:", cutoff)
print("\nClass counts:")
print(sub_df["TOTEXP23_binary"].value_counts().sort_index())
print("\nClass proportions:")
print(sub_df["TOTEXP23_binary"].value_counts(normalize=True).sort_index())

# Save the transformed dataframe to a new Stata file
sub_df.to_stata("data_column_subset.dta", write_index=False)