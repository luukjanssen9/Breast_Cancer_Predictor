import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report, confusion_matrix)
from sklearn.metrics import (mean_squared_error, accuracy_score, precision_score, recall_score)



df = pd.read_csv("brca.csv")
y = df['y']
df.drop('y', axis='columns', inplace=True)

#MinMaxScaler
scaler = MinMaxScaler(feature_range = (0,1))
model=scaler.fit(df)
scaled_data=model.transform(df)
scaled_data=pd.DataFrame(data = scaled_data, columns = df.columns)
df = scaled_data.join(y)

#Using top 5 features
X = df[['x.area_worst', 'x.concave_pts_worst', 'x.radius_worst', 'x.perimeter_worst', 'x.concave_pts_mean']]
y = df['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state = 42)


# Change B and M to 1 and 0
y_train = y_train.replace(['B'], 1)
y_train = y_train.replace(['M'], 0)
y_test = y_test.replace(['B'], 1)
y_test = y_test.replace(['M'], 0)

lr = LogisticRegression()
lr.fit(X_train, y_train)
predict = lr.predict(X_test)

#Classic metrics analysis
print(f"Classification report: \n {classification_report(y_test, predict)}")
print(f"Accuracy score: {accuracy_score(y_test, predict)} \n")

"""
matrix = confusion_matrix(y_test, predict)
TN, FP, FN, TP = matrix.ravel()
print(f"True Positives (TP): {TP}")
print(f"False Positives (FP): {FP}")
print(f"True Negatives (TN): {TN}")
print(f"False Negatives (FN): {FN} \n")

print(f"Recall - TP/(TP+FN): {TP/(TP+FN)}")
print(f"False Negative Rate - FN/(TP+FN): {FN/(TP+FN)}")
"""

"""
with open('models/lr_model.pkl', 'wb') as f:
    pickle.dump(classifier, f)

with open('models/lr_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
"""