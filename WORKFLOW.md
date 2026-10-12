# Project Workflow

## 1. Research Question and Study Design

### 1.1 Research Question and Dataset Overview

### 1.2 Adult Study Population and Eligibility Criteria

### 1.3 Baseline and Expanded Feature Sets

### 1.4 Outcome Definition and Evaluation Criteria

## 2. Data Preprocessing

### 2.1 Column Selection
Preserve person IDs; exclude IDs and survey weights from predictors.

### 2.2 Filtering for Adult Population

### 2.3 Inspection of Datatypes, Distributions, and Missing-Response Codes

### 2.4 Data Cleaning and Handling of Missing or Inapplicable Responses
Keep the same eligible observations for baseline and expanded comparisons.

### 2.5 Construction of TOTEXP23_binary from Original TOTEXP23 Column
Document the population used for the cutoff, treatment of ties, and whether the percentile is weighted.

### 2.6 Generate Stratified Training, Validation, and Test Partitioning Data Files
Record the seed and split proportions; verify that sets do not overlap.

## 3. Individual Model Training

### 3.1 Shared Observations for Baseline and Expanded Models

### 3.2 KNN: Baseline and Expanded Models
##### 3.2.1 Model-Specific Feature Preparation

##### 3.2.2 Hyperparameter Tuning and Validation

### 3.3 Logistic Regression: Baseline and Expanded Models

##### 3.3.1 Model-Specific Feature Preparation

##### 3.3.2 Hyperparameter Tuning and Validation

### 3.4 Decision Tree: Baseline and Expanded Models
##### 3.4.1 Model-Specific Feature Preparation

##### 3.4.2 Hyperparameter Tuning and Validation

### 3.5 Saving Model Pipelines and Predictions with Person IDs

## 4. Majority-Vote Ensembles

### 4.1 Baseline Ensemble: Combining the Three Baseline Models

### 4.2 Expanded Ensemble: Combining the Three Expanded Models

### 4.3 Prediction Alignment by Person ID

### 4.4 Comparison of Ensemble Validation Performance

### 4.5 Finalization of Hyperparameters and Voting Rules

## 5. Final Test Evaluation

### 5.1 Final Model Refitting and Test Predictions

### 5.2 Classification Metrics and Majority-Class Reference

### 5.3 Baseline, Expanded, and Ensemble Performance Comparisons

### 5.4 Uncertainty and Error Analysis

## 6. Interpretation and Limitations

### 6.1 Do Physical Activity and Smoking Improve Classification?

### 6.2 Interpretation of Model Results
Discuss missing-data exclusions and limitations of population claims without survey weighting.

### 6.3 Predictive Findings Versus Causal Claims

## 7. Final Report

### 7.1 Introduction and Research Question

### 7.2 Dataset and Study Population

### 7.3 Baseline and Expanded Modeling Methods

### 7.4 Ensemble Construction

### 7.5 Results, Tables, and Figures

### 7.6 Discussion and Limitations

### 7.7 Conclusion

### 7.8 References