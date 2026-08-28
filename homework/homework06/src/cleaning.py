import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Fills missing values in specified numerical columns with their median.
    """
    df = df.copy()
    for col in columns:
        if col in df.columns:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
    return df

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drops columns that have a missing value proportion higher than the threshold.
    """
    df = df.copy()
    return df.dropna(thresh=int((1 - threshold) * len(df)), axis=1)

def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Applies Min-Max scaling to normalize specified numerical columns between 0 and 1.
    """
    df = df.copy()
    for col in columns:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val != min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df