import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import pickle

# Import data
df = pd.read_csv('brca.csv')

# Initial exploration
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df['y'].value_counts())

# Remove unnecessary column
df = df.drop(df.columns[0], axis=1)

# Ensure consistent feature naming
df.columns = [col.replace('_pts_', '_points_') for col in df.columns]

# Create a new dataframe with only the selected columns
df = df[['x.area_worst', 'x.concave_points_worst', 'x.radius_worst',
         'x.perimeter_worst', 'x.concave_points_mean', 'y']]


# Split into X and Y
X = df.drop('y', axis=1)
Y = df["y"]

print(f"X head: {X.head()}")
print(f"Y head: {Y.head()}")

# Split the data into training and testing sets (80-20 split)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=37)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Change B and M to 1 and 0
Y_train = Y_train.replace(['B'], 1)
Y_train = Y_train.replace(['M'], 0)
Y_test = Y_test.replace(['B'], 1)
Y_test = Y_test.replace(['M'], 0)

# Fitting classifier to the Training set
classifier = SVC(kernel="linear", C=10, gamma=0.1, random_state=0, probability=True)
classifier.fit(X_train_scaled, np.asarray(Y_train))

print("Model trained with features:", X.columns.tolist())  # Add this in training script

# Evaluate the model
y_pred = classifier.predict(X_test_scaled)
print("Linear Kernel")
print(classification_report(Y_test, y_pred))

with open('models/svm_model.pkl', 'wb') as f:
    pickle.dump(classifier, f)

with open('models/svm_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")