# group3_data_mining_project
# Classification of High Healthcare Expenditure

This project uses the MEPS HC-251 2023 Full-Year Consolidated Data File to investigate whether physical activity and cigarette-smoking habits improve the classification of adults with high annual healthcare expenditures beyond age, sex, and insurance coverage.

## Dataset and Variables

The original dataset contains 18,919 observations and 1,374 variables. Our analysis focuses on adults aged 18 or older.

| Variable | Role |
|---|---|
| `TOTEXP23_binary` | Target: 1 = expenditure above the adult sample's 75th percentile; 0 = at or below it |
| `AGE23X` | Age |
| `SEX` | Sex |
| `INSCOV23` | Insurance coverage |
| `PHYEXE53` | Reported physical activity |
| `OFTSMK53` | Cigarette-smoking frequency |
| `POVCAT23` | Optional predictor: family income relative to the poverty line |
| `PERWT23F` | Survey weight; excluded from predictor features |
| `DUPERSID` | Person identifier for aligning predictions; excluded from predictor features |

The binary target is derived from `TOTEXP23`.

## Models and Ensembles

We train KNN, logistic regression, and decision tree classifiers using two feature sets:

- **Baseline:** age, sex, and insurance coverage.
- **Expanded:** baseline features plus physical activity and smoking.

This produces six individual models and two majority-vote ensembles: one combining the baseline models and another combining the expanded models. Each ensemble classifies an observation using the class predicted by at least two of its three members (three models let's us not need a tie breaker rule).

The ensembles aim to improve prediction by combining models whose errors may differ. Capable models make the baseline-versus-expanded comparison more informative, since weak models might fail to use useful information. However, improved prediction alone does not establish the value of the added features: both versions require comparable tuning, evaluation on the same test observations, and consideration of uncertainty. Findings concern predictive value, not causation.

## Training and Evaluation

All models use shared, stratified training, validation, and test splits with a fixed random seed. Models learn from training data, and validation data guide hyperparameter selection. Learned preprocessing is fitted on training data during tuning.

After all choices are finalized, models may be refitted on training and validation data together. Individual models and ensembles are then evaluated on the untouched test set using confusion matrices, precision, recall, F1 score, accuracy, and balanced accuracy.

We compare baseline versus expanded performance, ensembles versus their individual members, and all models against a majority-class reference classifier.
