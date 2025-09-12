import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def detect_outliers_isolation_forest(df, features, contamination=0.01):
    """Detect outliers using Isolation Forest"""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])
    
    model = IsolationForest(contamination=contamination, random_state=42)
    predictions = model.fit_predict(X_scaled)
    
    df['is_outlier'] = predictions
    df['is_outlier'] = df['is_outlier'].apply(lambda x: 1 if x == -1 else 0)
    
    return df

def analyze_fraud_patterns(df, target_column='is_fraud'):
    """Analyze patterns in fraudulent transactions"""
    if target_column not in df.columns:
        print(f"Target column '{target_column}' not found in dataframe")
        return
    
    # Compare fraudulent vs non-fraudulent transactions
    fraud_stats = df.groupby(target_column).agg({
        'amount': ['mean', 'std', 'min', 'max'],
        'user_id': 'count'
    }).round(2)
    
    print("Fraud Statistics:")
    print(fraud_stats)
    
    # Visualize distributions
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=target_column, y='amount', data=df[df['amount'] < df['amount'].quantile(0.99)])
    plt.title('Transaction Amount by Fraud Status')
    
    plt.subplot(1, 2, 2)
    sns.countplot(x=target_column, data=df)
    plt.title('Count of Fraud vs Non-Fraud Transactions')
    
    plt.tight_layout()
    plt.savefig('../results/fraud_analysis.png')
    plt.show()
    
    return fraud_stats
