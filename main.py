import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

