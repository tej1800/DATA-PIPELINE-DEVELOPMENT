# etl_pipeline.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Step 1: Extract - Load the data
def extract_data(filepath):
    print("Extracting data...")
    return pd.read_csv(filepath)

# Step 2: Transform - Preprocessing
def preprocess_data(df):
    print("Preprocessing data...")

    # Separate features and target (assuming the last column is the target)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Identify numeric and categorical columns
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Create transformers
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Combine transformers into a column transformer
    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    # Create a full pipeline
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor)
    ])

    X_transformed = pipeline.fit_transform(X)

    return X_transformed, y, pipeline

# Step 3: Load - Save processed data
def load_data(X, y, output_path="processed_data.csv"):
    print("Loading data...")
    # Convert to DataFrame if possible
    X_df = pd.DataFrame(X.toarray() if hasattr(X, "toarray") else X)
    y_df = pd.DataFrame(y).reset_index(drop=True)
    final_df = pd.concat([X_df, y_df], axis=1)
    final_df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

# Main ETL function
def run_etl_pipeline(filepath):
    df = extract_data(filepath)
    X, y, pipeline = preprocess_data(df)
    load_data(X, y)

# Example usage
if __name__ == "__main__":
    run_etl_pipeline("your_dataset.csv")  # Replace with your CSV file path
