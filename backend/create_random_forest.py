# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Load dataset
df = pd.read_csv("brca.csv")

# Display the first few rows
df.head()


# Drop ID column
df = df.drop(df.columns[0], axis=1)

# Convert 'diagnosis' to numerical values (M -> 1, B -> 0)
df['y'] = df['y'].map({'M': 0, 'B': 1})

# Drop the 'Unnamed: 32' column if it exists (some versions have an extra empty column)
df = df.dropna(axis=1)

# Check dataset info
df.info()

# Ensure consistent feature naming
df.columns = [col.replace('_pts_', '_points_') for col in df.columns]

# Create a new dataframe with only the selected columns
df = df[['x.area_worst', 'x.concave_points_worst', 'x.radius_worst',
         'x.perimeter_worst', 'x.concave_points_mean', 'y']]

df.info()
# Define features and target variable
X = df.drop(columns=['y'])  # Features (all except target)
y = df['y']  # Target (M=1, B=0)

# Split dataset into training and test sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Check the distribution of classes in train and test sets
print(y_train.value_counts(), y_test.value_counts())

# Standardize the dataset
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = rf_model.predict(X_test_scaled)

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

# Get feature importance
feature_importances = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values(ascending=False)

# Plot feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances.values, y=feature_importances.index, hue=feature_importances.index, palette="coolwarm", legend=False)
plt.xlabel("Importance Score")
plt.ylabel("Feature Name")
plt.title("Feature Importance in Random Forest")
plt.show()

# Evaluate model performance
y_pred = rf_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"Random Forest Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))


with open('models/rf_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

with open('models/rf_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")