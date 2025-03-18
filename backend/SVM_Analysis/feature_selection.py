import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

brca_data = pd.read_csv('../brca.csv')
brca_data = brca_data.drop(brca_data.columns[0], axis=1)
brca_data
features = brca_data.iloc[:, :-1]  # Select all columns except the last one as features
result = brca_data.iloc[:, -1]   # Select the last column as the target
feature_names = features.columns.tolist()  # Get feature names

X_train, X_test, y_train, y_test = train_test_split( features, result, test_size = 0.25, random_state=42) # Split dataset into 75% train and 25% test
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

importances = clf.feature_importances_
feature_imp_df = pd.DataFrame({'Feature': feature_names, 'Gini Importance': importances}).sort_values('Gini Importance', ascending=False) 
print(feature_imp_df)