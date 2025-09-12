# Fraud Pattern Detection Analysis

## Project Overview
This project conducts a comprehensive analysis of credit card transaction data to identify patterns and anomalies indicative of fraudulent activity. Using a hypothesis-driven approach, the analysis leverages both SQL for data exploration and Python for statistical analysis and machine learning. The project demonstrates an end-to-end data science workflow from data acquisition to model evaluation.

**Key Questions/Hypotheses Tested:**
1. Do fraudulent transactions have different amount distributions than legitimate ones?
2. Does fraud occur more frequently during specific times of day?
3. Can machine learning models effectively detect fraud patterns in highly imbalanced data?

## Dataset
**Source:** [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) from Kaggle.

**Description:**
The dataset contains 284,807 transactions made by European cardholders in September 2013, with only 492 (0.172%) fraudulent transactions, making this a highly imbalanced classification problem. The dataset contains 31 features:

- **Time:** Seconds elapsed between transaction and first transaction
- **Amount:** Transaction amount
- **V1-V28:** Principal components from PCA transformation (anonymized features)
- **Class:** Target variable (1 = Fraud, 0 = Legitimate)

## Technologies Used
- **Python** (pandas, NumPy, scikit-learn, Matplotlib, Seaborn)
- **Jupyter Notebook** for interactive analysis and reporting
- **MySQL** with **MySQL Workbench** for SQL exploration
- **Isolation Forest** algorithm for unsupervised anomaly detection
- **Random Forest** classifier for supervised fraud prediction
- **SQLAlchemy** for Python-SQL database connectivity
- **Git** for version control



## Methodology

### 1. Data Acquisition & Storage
- Downloaded dataset from Kaggle using the Kaggle API
- Loaded data into a MySQL database using MySQL Workbench's Table Data Import Wizard
- Created an optimized database schema for efficient querying

### 2. SQL Exploration (MySQL Workbench)
- Performed initial data exploration using SQL queries
- Conducted hypothesis testing through aggregate analysis
- Analyzed time-based patterns and transaction distributions
- Developed and saved reproducible SQL queries for all analyses

### 3. Python Analysis (Jupyter Notebook)
- Conducted comprehensive exploratory data analysis (EDA)
- Handled class imbalance through stratified sampling
- Engineered features for improved model performance
- Developed and evaluated multiple machine learning models

### 4. Model Development
- Implemented Logistic Regression as a baseline model
- Trained Random Forest classifier for improved performance
- Addressed class imbalance using class weighting
- Evaluated models using precision, recall, F1-score, and ROC-AUC

### 5. Analytical Approach
The project employed a tiered methodology:
1. **Exploratory Analysis (SQL):** Hypothesis-driven pattern discovery in MySQL Workbench
2. **Anomaly Detection (Isolation Forest):** Unsupervised learning to identify unusual transaction patterns
3. **Predictive Modeling (Random Forest):** Supervised learning for precise fraud classification
4. **Validation:** Cross-validation of findings across multiple techniques

This multi-method approach ensured robust pattern validation and comprehensive fraud coverage.

## Key Findings & Results

### Statistical Validation of Hypotheses
- **Hypothesis 1 (Amount):** CONFIRMED (p = 0.0032). Fraudulent transactions show statistically significant different amount patterns.
- **Hypothesis 2 (Time):** STRONGLY CONFIRMED. Fraud rate during peak hours (2-4 AM) is **0.98%**, which is **6.98x higher** than non-peak hours (0.14%).

### SQL Analysis Results
- **Time Patterns:** Fraudulent transactions peak dramatically during late night hours, with the highest fraud rate at **2 AM (1.59%)** — 9 times higher than the daily average.
- **Amount Analysis:** High-value transactions ($500+) have the highest fraud rate at **0.4187%** — 2.4 times higher than lower-value transactions.
- **Fraud Concentration:** 50% of all fraud occurs between 1 AM and 5 AM, indicating clear temporal patterns.

### Machine Learning Results
- **Random Forest Performance:**
  - Precision: 0.95
  - Recall: 0.85
  - F1-Score: 0.90
  - ROC-AUC: 0.98
- **Key Features:** V17, V14, V12, V10, and Amount were most important for detection.

### Outlier Detection Results
- **Anomaly Significance:** Transactions flagged as outliers were **287 times more likely** to be fraudulent (12.37% fraud rate vs. 0.043% for normal transactions).
- **Fraud Coverage:** The Isolation Forest algorithm detected **74.2% of all fraudulent transactions** (351 out of 473 fraud cases).

## Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- MySQL Workbench (optional but recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fraud-pattern-detection.git
cd fraud-pattern-detection


### 2. Create Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate


### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Database Setup
sql
CREATE DATABASE fraud_detection;
USE fraud_detection;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Time FLOAT,
    V1 FLOAT, V2 FLOAT, V3 FLOAT, V4 FLOAT, V5 FLOAT, V6 FLOAT, V7 FLOAT, V8 FLOAT, V9 FLOAT,
    V10 FLOAT, V11 FLOAT, V12 FLOAT, V13 FLOAT, V14 FLOAT, V15 FLOAT, V16 FLOAT, V17 FLOAT, V18 FLOAT, V19 FLOAT,
    V20 FLOAT, V21 FLOAT, V22 FLOAT, V23 FLOAT, V24 FLOAT, V25 FLOAT, V26 FLOAT, V27 FLOAT, V28 FLOAT,
    Amount FLOAT,
    Class INT
);

### 5. Data Import
    Download creditcard.csv from Kaggle

    Use MySQL Workbenchs Table Data Import Wizard or run:

```bash
python scripts/load_to_mysql.py
  
    
### Usage

# 1. SQL Exploration (MySQL Workbench)

- Open MySQL Workbench and connect to your local database.

- Execute queries from scripts/sql_analysis_queries.sql.

- Explore data relationships and test hypotheses.


# 2. Python Analysis
```bash
jupyter lab


# 3. Run Specific Analyses
```bash
python scripts/sql_queries.py
python scripts/analysis.py






Conclusion

This project successfully identified clear, actionable patterns in fraudulent activity through SQL analysis and machine learning. The analysis revealed that:

  - Temporal Patterns: Fraud peaks at 2 AM with a 1.59% fraud rate, 9 times higher than average.

  - Amount Correlations: $500+ transactions have 2.4 times higher fraud incidence.

  - Feature Importance: Time of day and transaction amount are critical predictors alongside PCA components.

The Random Forest model achieved excellent performance (F1-Score: 0.90, ROC-AUC: 0.98) in detecting fraudulent transactions while maintaining high precision to minimize false positives. The findings provide concrete recommendations for targeted fraud monitoring, particularly during high-risk hours (1-5 AM) and for high-value transactions.

This analysis demonstrates the power of combining SQL for pattern discovery with machine learning for predictive modeling in fraud detection scenarios.

