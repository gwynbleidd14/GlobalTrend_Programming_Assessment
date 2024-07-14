'''
4. Using pandas, write a Python function to clean and preprocess a given DataFrame,
which involves handling missing values, normalizing numerical columns, and encoding
categorical columns.
'''

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(csv_file):
    df = pd.read_csv("D:\Desktop\Global Trend Assignment\Assessment\data.csv")
    df.fillna(method='ffill', inplace=True)
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    return df


file_path = 'sample_data.csv'
processed_data = preprocess_data(file_path)
print(processed_data.head())