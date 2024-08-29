# Feature_Selection_Project
"All  project in this Repository focused on selecting the most significant features for machine learning models"\
To perform Filter-based feature selection:

1.Duplicate Features:

Identify and remove duplicate columns from the dataset. Columns with identical values provide redundant information and do not contribute to the prediction task.\
2.Variance Threshold Method:

Calculate the variance of each feature.\
Remove features with low variance, as they tend to have little or no predictive power.\
Set a threshold value for variance and remove features below that threshold.\
3.Correlation:

Compute the correlation matrix of the features.\
Identify highly correlated features and choose one from each highly correlated group.\
High correlation between features indicates redundancy, and removing one from each correlated group helps reduce multicollinearity.
4.ANOVA (Analysis of Variance):

Perform an ANOVA test between each feature and the target variable ("Pass/Fail").\
Select features with a significant impact on the target variable.\
Set a significance level (e.g., p-value threshold) for the test to determine the importance of each feature.

5.Chi-Squared:

Apply the Chi-Squared test between each feature and the target variable, considering both features as categorical.\
Select features with a significant association with the target variable.\
Set a significance level (e.g., p-value threshold) to determine the importance of each feature.

**Wrapper Methods:**
Iteratively select features by evaluating model performance, such as:

1.Forward Selection: Start with no features, add one at a time that improves model performance.\
2.Backward Elimination: Start with all features, remove the least significant one iteratively.\
3.Recursive Feature Elimination (RFE): Recursively build a model and remove the weakest feature until the desired number of features is reached.
**Embedded Methods: **
Feature selection occurs during the model training process:

1.Lasso Regression (L1 Regularization): Penalizes the absolute size of coefficients, driving some to zero, effectively selecting features.\
2.Tree-based Methods: Models like Random Forests or Gradient Boosted Trees rank feature importance during training.
