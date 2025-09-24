import pandas as pd
from pandas.io.formats.style import Styler


def generate_data_dictionary(df: pd.DataFrame, sample_row: int = 0) -> pd.DataFrame:
    """Generate a data dictionary from a DataFrame.
    
    Args:
        df (pd.DataFrame): An input DataFrame.
        sample_row (int): Row index to source sample values from.
    
    Returns:
        pd.DataFrame: A simple data dictionary
    """
    data_dict = pd.DataFrame({
        'Data Type': df.dtypes.astype(str),
        'Missing Values': df.isnull().sum().values,
        'Unique Values': df.nunique().values,
        'Sample Value': df.iloc[sample_row].values
    }, index=df.columns)
    
    data_dict.index.name = 'Column Name'

    return data_dict