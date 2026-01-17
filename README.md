# Customer-Churn-Prediction
Built a machine learning model to predict customer churn using historical customer data. The project covers data cleaning, exploratory data analysis, feature encoding, train-test splitting, model training, and evaluation. The model helps businesses identify customers who are likely to leave and supports data-driven retention strategies.
📌 Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their services. This project uses machine learning to predict churn based on customer demographics, service usage, and billing details.

🎯 Objective

To build a machine learning model that predicts whether a customer will churn or not, based on historical customer data.

🗂 Dataset

Dataset: Telco Customer Churn

Source: Kaggle

Target Column: Churn

Yes → Customer churned

No → Customer retained

⚙️ Tools & Libraries Used

Python

Pandas

NumPy

Matplotlib & Seaborn

Scikit-learn

🧪 Step-by-Step Implementation 
✅ Step 1: Import Required Libraries

Used Python libraries for data handling, visualization, and machine learning.

✅ Step 2: Load the Dataset

The dataset is loaded using Pandas to begin analysis.

✅ Step 3: Understand the Data

Checked:

Shape of dataset

Column names

Data types

Missing values

This helps in understanding the structure of the data.

✅ Step 4: Drop Unnecessary Columns

customerID was removed because it is a unique identifier and does not help in prediction.

✅ Step 5: Handle Missing Values

Missing values were identified and handled to avoid errors during model training.

✅ Step 6: Convert Target Variable

The Churn column was converted into numerical form:

Yes → 1

No → 0

This is required for machine learning models.

✅ Step 7: Exploratory Data Analysis (EDA)

Performed EDA to understand churn patterns using:

Count plots

Distribution plots

Key insights were drawn about churn behavior.

✅ Step 8: Encode Categorical Features

Categorical columns were converted into numerical format using encoding techniques so that ML models can process them.

✅ Step 9: Feature & Target Separation
X = df.drop('Churn', axis=1)
y = df['Churn']


X → Input features

y → Output (Churn)

✅ Step 10: Train-Test Split

The dataset was split into training and testing sets to evaluate model performance on unseen data.

✅ Step 11: Feature Scaling

Numerical features were scaled using fit_transform() to ensure all features are on the same scale.

✅ Step 12: Model Training

A machine learning model (Logistic Regression / Random Forest) was trained using the training data.
