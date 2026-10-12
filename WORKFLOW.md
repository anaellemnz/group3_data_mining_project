# Project Workflow

## 1. Research Question and Study Design

### Research Question

### MEPS HC-251 Dataset Overview

### Adult Study Population and Eligibility Criteria

### Baseline Features: Age, Sex, and Insurance Coverage

### Expanded Features: Baseline Plus Physical Activity and Smoking

### Decision on Including Poverty Category in Both Feature Sets

### Definition of High Healthcare Expenditure

### Evaluation Metrics and Comparison Criteria

## 2. Data Preprocessing

### Column Selection and Preservation of Person IDs

### Inspection of Datatypes, Distributions, and Missing-Response Codes

### Adult Population Filtering

### Data Cleaning and Handling of Missing or Inapplicable Responses

### Documentation of Excluded Observations

### Construction of TOTEXP23_binary Using the Adult Sample

### Removal of Original Expenditure from Modeling Data

### Shared Stratified Training, Validation, and Test Partitioning

### Saving and Sharing the Splits as Stata Files

## 3. Individual Model Training

### Shared Observations for Baseline and Expanded Models

### Categorical Encoding, Scaling, and Imputation

### KNN: Baseline and Expanded Models

### Logistic Regression: Baseline and Expanded Models

### Decision Tree: Baseline and Expanded Models

### Hyperparameter Tuning Using Training and Validation Data

### Comparison of Validation Performance

### Saving Model Pipelines and Predictions with Person IDs

## 4. Majority-Vote Ensembles

### Baseline Ensemble: Combining the Three Baseline Models

### Expanded Ensemble: Combining the Three Expanded Models

### Prediction Alignment by Person ID

### Comparison of Ensemble Validation Performance

### Finalization of Hyperparameters and Voting Rules

## 5. Final Test Evaluation

### Final Refitting on Training and Validation Data

### Evaluation on the Shared Untouched Test Set

### Majority-Class Reference Classifier

### Confusion Matrices, Precision, Recall, and F1 Scores

### Accuracy and Balanced Accuracy

### Baseline Versus Expanded Comparison Within Each Algorithm

### Baseline Versus Expanded Ensemble Comparison

### Ensemble Versus Individual Model Comparison

### Uncertainty in Performance Differences

### Error Analysis

## 6. Interpretation and Limitations

### Do Physical Activity and Smoking Improve Classification?

### Interpretation of Model Results

### Class Imbalance and Missing-Data Limitations

### Survey Weights and Population Generalizability

### Household Dependence Across Observations

### Same-Year Associations Versus Future Prediction

### Predictive Findings Versus Causal Claims

## 7. Final Report

### Introduction and Research Question

### Dataset and Study Population

### Data Preparation and Exclusions

### Baseline and Expanded Modeling Methods

### Ensemble Construction

### Results, Tables, and Figures

### Discussion and Limitations

### Conclusion

### References

## 8. Reproducibility and Team Coordination

### Team Responsibilities

### Script Execution Order

### Dependencies and Random Seeds

### Shared Data Versions and Model Artifacts

### README and Instructions for Reproducing Results

### Final Review of Code and Report