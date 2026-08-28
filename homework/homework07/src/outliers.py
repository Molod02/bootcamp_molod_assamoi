import pandas as pd
import numpy as np

def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Returns boolean mask for IQR-based outliers.
    Improved: valid parameter checking and handles empty series/NaN values cleanly.
    """
    if k <= 0:
        raise ValueError("Parameter k must be positive.")
    if series.empty:
        return pd.Series([], dtype=bool)
        
    s_clean = series.dropna()
    q1 = s_clean.quantile(0.25)
    q3 = s_clean.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    
    return (series < lower) | (series > upper)

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    Returns boolean mask for Z-score outliers where |z| > threshold.
    Improved: uses sample std (ddof=1) for sample data and handles zero variance.
    """
    if threshold <= 0:
        raise ValueError("Threshold must be positive.")
    if series.empty:
        return pd.Series([], dtype=bool)
        
    mu = series.mean()
    sigma = series.std(ddof=1)
    if sigma == 0 or pd.isna(sigma):
        return pd.Series(False, index=series.index)
        
    z = (series - mu) / sigma
    return z.abs() > threshold

def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    """
    Clips series values outside the given quantile bounds.
    Improved: checks that lower quantile < upper quantile.
    """
    if not (0 <= lower < upper <= 1):
        raise ValueError("Quantile bounds must satisfy 0 <= lower < upper <= 1.")
    
    lo = series.quantile(lower)
    hi = series.quantile(upper)
    return series.clip(lower=lo, upper=hi)