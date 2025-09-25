import pandas as pd
import os

RAW_ACCEPTED = "data/accepted_2007_to_2018Q4.csv"
CACHE_ACCEPTED = "cache/accepted.parquet"

RAW_REJECTED = "data/rejected_2007_to_2018Q4.csv"
CACHE_REJECTED = "cache/rejected.parquet"

def load_accepted(use_cache=True) -> pd.DataFrame:
    """Read either data/csv or cache/parquet of accepted loan data into dataframe.
    
    Args:
        use_cache (boolean): If true, cached parquet format data is read into the df (improved speed)

    Returns:
        DataFrame: A DataFrame object containing accepted loan data
    """
    if use_cache and os.path.exists(CACHE_ACCEPTED):
        return pd.read_parquet(CACHE_ACCEPTED)
    
    df = pd.read_csv(RAW_ACCEPTED, low_memory=False)
    df.to_parquet(CACHE_ACCEPTED)
    return df

def load_rejected(use_cache=True) -> pd.DataFrame:
    """Read either data/csv or cache/parquet of rejected loan data into dataframe.
    
    Args:
        use_cache (boolean): If true, cached parquet format data is read into the df (improved speed)

    Returns:
        DataFrame: A DataFrame object containing rejected loan data
    """
    if use_cache and os.path.exists(CACHE_REJECTED):
        return pd.read_parquet(CACHE_REJECTED)
    
    df = pd.read_csv(RAW_REJECTED, low_memory=False)
    df.to_parquet(CACHE_REJECTED)

    return df