import pandas as pd
import numpy as np

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Engineers Stage 09 features: spend_income_ratio, log_income, and region one-hot encoding.
    """
    df_out = df.copy()
    
    # Feature 1: Spend-to-Income Ratio
    if 'monthly_spend' in df_out.columns and 'income' in df_out.columns:
        df_out['spend_income_ratio'] = df_out['monthly_spend'] / df_out['income']
        
    # Feature 2: Log-transformed Income
    if 'income' in df_out.columns:
        df_out['log_income'] = np.log1p(df_out['income'])
        
    # Feature 3: Categorical One-Hot Encoding
    if 'region' in df_out.columns:
        df_out = pd.get_dummies(df_out, columns=['region'], prefix='region', dtype=int)
        
    return df_out