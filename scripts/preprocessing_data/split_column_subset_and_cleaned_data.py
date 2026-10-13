from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

SEED = 42
TARGET = "target"  

df = pd.read_stata("data_column_subset.dta", convert_categoricals=False)

# Keep an existing unique identifier if available.
df.insert(0, "row_id", range(len(df)))

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

output = Path("data/splits")
output.mkdir(parents=True, exist_ok=True)

for name, split in [
    ("train", train),
    ("validation", validation),
    ("test", test),
]:
    split.to_stata(
        output / f"{name}.dta",
        write_index=False,
        version=118,
    )

    print(f"{name}: {len(split)} rows")
    print(split[TARGET].value_counts(normalize=True).sort_index())
