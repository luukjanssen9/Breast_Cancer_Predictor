import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler

# import data
df = pd.read_csv('brca.csv')

# Initial exploration
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

print(df['y'].value_counts())

# Remove unnecassary column
df = df.drop(df.columns[0], axis=1)

# Split into X and Y
X = df.iloc[:, :-1]
Y = df["y"]

print(f"X head: {X.head()}")
print(f"Y head: {Y.head()}")


# Split the data into training and testing sets (80-20 split)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Scale the data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Change B and M to 1 and 0
Y_train = Y_train.replace(['B'], 1)
Y_train = Y_train.replace(['M'], 0)
Y_test = Y_test.replace(['B'], 1)
Y_test = Y_test.replace(['M'], 1)

print(f"X_train: {X_train}")
print(f"X_test: {X_test}")
print(f"Y_train: {Y_train.head()}")
print(f"Y_test: {Y_test.head()}")


# Fitting classifier to the Training set
classifier = SVC(random_state=0) # for non-linear model use this parametre kernel='rbf'
classifier.fit(X_train, Y_train)

# Predicting the Test set results
Y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(Y_test, Y_pred)
