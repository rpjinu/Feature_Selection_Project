# -*- coding: utf-8 -*-
"""Dim_reduction(credit_card_dataset).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GXXDdSQ5bleOxJp-41reWjUeC8d-xfDY
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold, SelectKBest, mutual_info_classif
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

"""#load dataset"""

df=pd.read_csv('/content/Fraud_Detection_DataSet _reduce_dimension.csv')
df.head()

df.info()

#class column float to integer
df['Class'] = df['Class'].astype(int)

df.shape

df.duplicated().sum()

#drop dupliacted row
df.drop_duplicates(inplace=True)

# Transpose the DataFrame to make columns as rows, then find duplicates
df.T.duplicated().any()

df.shape

df.isnull().sum().any()

df.describe()

y.value_counts()

colors = ['#1f77b4', '#ff7f0e']
# Plotting the class distribution
sns.countplot(x='Class', data=df, palette=colors)
plt.title('Class Distributions \n (0: No Fraud || 1: Fraud)', fontsize=14)
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Separate features and label
X = df.drop(columns=['Class'])
y = df['Class']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

"""#PCA (Principal Component Analysis)"""

# Standardize the data (important for PCA and other methods)
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

# Apply PCA
pca = PCA(n_components=10)
X_train_pca = pca.fit_transform(X_train_sc)
X_test_pca = pca.transform(X_test_sc)

# Train a classifier (Random Forest in this case)
clf_pca = RandomForestClassifier(random_state=42)
clf_pca.fit(X_train_pca, y_train)
y_pred_pca = clf_pca.predict(X_test_pca)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred_pca)
print("Accuracy:", accuracy)
print("PCA Performance:")
print(classification_report(y_test, y_pred_pca))

"""#SelectKBest"""

# Apply SelectKBest
select_k_best = SelectKBest(mutual_info_classif, k=10)
X_train_best = select_k_best.fit_transform(X_train_sc, y_train)
X_test_best = select_k_best.transform(X_test_sc)

# Train classifier on selected features
clf_best = RandomForestClassifier(random_state=42)
clf_best.fit(X_train_best, y_train)
y_pred_best = clf_best.predict(X_test_best)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred_best)
print("Accuracy:", accuracy)
print("SelectKBest Performance:")
print(classification_report(y_test, y_pred_best))

"""#As per Accuracy best model here for feature reduction is "select_K_best" apply again on data then save it as per project requirement"""

X_scaled = scaler.fit_transform(X)

# Apply SelectKBest (keep top 10 features)
select_k_best = SelectKBest(mutual_info_classif, k=10)
X_reduced = select_k_best.fit_transform(X_scaled, y)

X_reduced

# Get the selected feature names
selected_feature_indices = select_k_best.get_support(indices=True)
features_name= X.columns[selected_feature_indices]

features_name

# Create a DataFrame with the reduced features
X_reduced_df = pd.DataFrame(X_reduced, columns=features_name)

#add the y data set in X
X_reduced_df['Class'] = y

X_reduced_df.head()

#copy reduce dataset df2
df2=X_reduced_df.copy()

# Save the reduced dataset to a CSV file
df2.to_csv('reduced_dataset.csv', index=False)
print("Reduced dataset saved as 'fraud_detection_reduced.csv'.")

