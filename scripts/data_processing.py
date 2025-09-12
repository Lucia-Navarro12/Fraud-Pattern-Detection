import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data_from_csv(file_path):
    """Load dataset from CSV file"""
    df = pd.read_csv(file_path)
    return df

def load_data_from_sql(query, connection_string):
    """Load data from SQL database"""
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df

def clean_data(df):
    """Clean the dataset"""
    # Handle missing values
    df = df.dropna()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert date columns if needed
    date_columns = df.select_dtypes(include=['object']).filter(like='date').columns
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    
    return df

def feature_engineering(df):
    """Create new features for fraud detection"""
    # Example: transaction frequency per user
    if 'user_id' in df.columns and 'transaction_date' in df.columns:
        df['transaction_count'] = df.groupby('user_id')['user_id'].transform('count')
    
    # Example: transaction amount statistics
    if 'amount' in df.columns and 'user_id' in df.columns:
        df['avg_amount'] = df.groupby('user_id')['amount'].transform('mean')
        df['amount_std'] = df.groupby('user_id')['amount'].transform('std')
        df['amount_zscore'] = (df['amount'] - df['avg_amount']) / df['amount_std']
    
    return df
