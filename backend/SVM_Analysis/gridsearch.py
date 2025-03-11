import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pickle

# Import data
df = pd.read_csv('../brca.csv')

# Initial exploration
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df['y'].value_counts())

# Remove unnecessary column
df = df.drop(df.columns[0], axis=1)

# Split into X and Y
X = df[["x.area_worst", "x.concave_pts_worst", "x.radius_worst", "x.perimeter_worst", "x.concave_pts_mean"]]
Y = df["y"]

print(f"X head: {X.head()}")
print(f"Y head: {Y.head()}")

# Split the data into training and testing sets (80-20 split)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Change B and M to 1 and 0
Y_train = Y_train.replace(['B'], 1)
Y_train = Y_train.replace(['M'], 0)
Y_test = Y_test.replace(['B'], 1)
Y_test = Y_test.replace(['M'], 0)

# Hyperparameter Tuning with GridSearchCV
param_grid = {'C': [0.1, 10, 100, 1000, 5000],
              'gamma': [0.1, 0.01, 0.001, 0.0001, 1],
              'kernel': ['linear', 'poly', 'sigmoid']}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=3)

# Fit the model using GridSearchCV
grid.fit(X_train_scaled, Y_train)

# Get the best model
best_classifier = grid.best_estimator_

# Fitting the best classifier to the Training set
best_classifier.fit(X_train_scaled, np.asarray(Y_train))

print("Model trained with features:", X.columns.tolist())  # Add this in training script

# Evaluate the model
y_pred = best_classifier.predict(X_test_scaled)
print("Best Kernel:", grid.best_params_['kernel'])
print("Best C:", grid.best_params_['C'])
print("Best Gamma:", grid.best_params_['gamma'])
print("Classification Report:")
print(classification_report(Y_test, y_pred))

# Save the model and scaler
pickle.dump(best_classifier, open('svm_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model and scaler saved successfully!")
