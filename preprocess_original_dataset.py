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
