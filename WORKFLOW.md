# Project Workflow

## 1. Research Question and Study Design

### Research Question and Dataset Overview

### Adult Study Population and Eligibility Criteria

### Baseline and Expanded Feature Sets

### Outcome Definition and Evaluation Criteria

## 2. Data Preprocessing

### Column Selection 

### Filtering for Adult Population

### Inspection of Datatypes, Distributions, and Missing-Response Codes

### Data Cleaning and Handling of Missing or Inapplicable Responses

### Construction of TOTEXP23_binary from Original TOTEXP23 Column

### Generate Stratified Training, Validation, and Test Partitioning Data Files 


## 3. Individual Model Training

### Shared Observations for Baseline and Expanded Models

### KNN: Baseline and Expanded Models

### Logistic Regression: Baseline and Expanded Models

### Decision Tree: Baseline and Expanded Models

### Saving Model Pipelines and Predictions with Person IDs

## 4. Majority-Vote Ensembles

### Baseline Ensemble: Combining the Three Baseline Models

### Expanded Ensemble: Combining the Three Expanded Models

### Prediction Alignment by Person ID

### Comparison of Ensemble Validation Performance

### Finalization of Hyperparameters and Voting Rules

## 5. Final Test Evaluation

### Final Model Refitting and Test Predictions

### Classification Metrics and Majority-Class Reference

### Baseline, Expanded, and Ensemble Performance Comparisons

### Uncertainty and Error Analysis

## 6. Interpretation and Limitations

### Do Physical Activity and Smoking Improve Classification?

### Interpretation of Model Results

### Predictive Findings Versus Causal Claims

## 7. Final Report

### Introduction and Research Question

### Dataset and Study Population

### Baseline and Expanded Modeling Methods

### Ensemble Construction

### Results, Tables, and Figures

### Discussion and Limitations

### Conclusion

### References