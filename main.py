import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

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

# TODO: preprocess data

# Split into X and Y
X = df.iloc[:, :-1]
Y = df["y"]

print(f"X head: {X.head()}")
print(f"Y head: {Y.head()}")


# Split the data into training and testing sets (80-20 split)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
