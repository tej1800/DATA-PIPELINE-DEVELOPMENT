# DATA-PIPELINE-DEVELOPMENT
*COMPANY*: CODETECH IT SOLUTIONS
*NAME*: TEJAS RODE
*INTERN ID*: CT1MTWK168
*DOMAIN*: DATA SCIENCE
*DURATION* : 4 WEEKS
*MENTOR*: NEELA SANTOSH

ETL Pipeline using Pandas and Scikit-learn
The goal of this project is to design and implement an automated ETL (Extract, Transform, Load) pipeline using Python, leveraging popular data science libraries such as Pandas and Scikit-learn. This pipeline streamlines the process of preparing raw data for machine learning and analytics, ensuring that the data is clean, consistent, and ready for modeling or storage.

1. Extract (Data Ingestion)
The first step in the pipeline is data extraction. This involves reading raw data from a source file, typically a .csv file. We use Pandas, a powerful data manipulation library, to load the dataset into a DataFrame. The script is designed to handle structured tabular data with both numeric and categorical variables. The function extract_data() handles this process and prepares the dataset for further processing.

2. Transform (Data Preprocessing & Transformation)
This stage is the core of the ETL pipeline and involves multiple preprocessing tasks:

Missing Value Handling: Many real-world datasets have missing values that must be addressed. We use Scikit-learn’s SimpleImputer to fill missing numeric values with the mean and categorical values with the most frequent category.

Feature Scaling: To normalize numeric features and bring them onto the same scale, we apply StandardScaler. This is important for many machine learning algorithms that are sensitive to the scale of input features.

Categorical Encoding: Categorical features are transformed using OneHotEncoding, which converts string labels into binary vectors, allowing models to process categorical variables effectively.

Pipeline and ColumnTransformer: To apply different transformations to numeric and categorical columns, we use Scikit-learn's ColumnTransformer. The full preprocessing logic is wrapped in a Scikit-learn Pipeline, making the process modular, reusable, and clean.

The function preprocess_data() executes this transformation step and returns a processed feature matrix X, the target variable y, and the complete transformation pipeline for reuse or deployment.

3. Load (Saving Processed Data)
Once the data is preprocessed and transformed, it is saved in a structured format. We use Pandas again to save the cleaned and transformed dataset into a new .csv file using the load_data() function. This simulates the "Load" part of an ETL system, where the data is stored in a format ready for modeling or analysis.

The script saves the transformed data with both features and labels, ensuring it's in a usable format for future machine learning tasks or reporting.

Modularity and Automation
The entire process is automated within a script, using a function run_etl_pipeline() that connects all the steps: extraction, transformation, and loading. The code is modular and can easily be integrated into larger data workflows or scheduled as a part of a data pipeline.

This ETL pipeline serves as a robust foundation for any data science or machine learning workflow. It ensures that the data is clean, well-formatted, and ready for modeling, helping teams reduce manual effort and focus on building better models and insights.

