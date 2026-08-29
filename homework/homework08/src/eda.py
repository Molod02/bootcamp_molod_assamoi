import pandas as pd
import numpy as np

def eda_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a unified statistical and structural summary table for any DataFrame.
    Flags missingness, unique counts, data types, and potential modeling issues.
    """
    summary = pd.DataFrame({
        'dtype': df.dtypes,
        'non_null_count': df.notnull().sum(),
        'null_count': df.isnull().sum(),
        'null_pct': (df.isnull().sum() / len(df) * 100).round(2),
        'nunique': df.nunique(),
    })
    
    # Identify warnings for feature engineering (stage 09)
    flags = []
    for col in df.columns:
        col_flags = []
        if summary.loc[col, 'null_pct'] > 20:
            col_flags.append('High Missingness (>20%)')
        if summary.loc[col, 'nunique'] == 1:
            col_flags.append('Zero Variance (Single Value)')
        elif summary.loc[col, 'nunique'] == len(df):
            col_flags.append('High Cardinality / ID Column')
        
        # Check if one category dominates (>90% of observations)
        if not pd.api.types.is_numeric_dtype(df[col]):
            top_freq = df[col].value_counts(normalize=True).max() if not df[col].empty else 0
            if top_freq > 0.9:
                col_flags.append(f'Dominant Category ({top_freq*100:.1f}%)')
                
        flags.append(', '.join(col_flags) if col_flags else 'OK')
        
    summary['flags'] = flags
    return summary