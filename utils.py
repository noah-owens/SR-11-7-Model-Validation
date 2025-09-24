import pandas as pd

def generate_data_dictionary(df: pd.DataFrame, sample_row: int = 0) -> pd.DataFrame:
    """Generate a data dictionary from a DataFrame.
    
    Args:
        df (pd.DataFrame): An input DataFrame.
        sample_row (int): Row index to source sample values from.
    
    Returns:
        pd.DataFrame: A simple data dictionary
    """
    data_dict = pd.DataFrame({
        'Column Name': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Missing Values': df.isnull().sum().values,
        'Unique Values': df.nunique().values,
        'Sample Value': df.iloc[sample_row].values
    })

    return data_dict

