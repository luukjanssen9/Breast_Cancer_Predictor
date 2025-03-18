import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Load dataset
df = pd.read_csv("brca.csv")

# Drop ID column
df = df.drop(df.columns[0], axis=1)

# Convert 'diagnosis' to numerical values (M -> 1, B -> 0)
df['y'] = df['y'].map({'M': 0, 'B': 1})

# Drop the 'Unnamed: 32' column if it exists
df = df.dropna(axis=1)

# Ensure consistent feature naming
df.columns = [col.replace('_pts_', '_points_') for col in df.columns]

# Select relevant features
df = df[['x.area_worst', 'x.concave_points_worst', 'x.radius_worst',
         'x.perimeter_worst', 'x.concave_points_mean', 'y']]

# Define features and target variable
X = df.drop(columns=['y'])
y = df['y']

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the dataset
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Logistic Regression model
log_model = LogisticRegression(random_state=42, max_iter=1000)
log_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = log_model.predict(X_test_scaled)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# Display classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Display confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', xticklabels=['Benign', 'Malignant'], yticklabels=['Benign', 'Malignant'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Save model and scaler
with open('models/log_model.pkl', 'wb') as f:
    pickle.dump(log_model, f)

with open('models/log_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")
