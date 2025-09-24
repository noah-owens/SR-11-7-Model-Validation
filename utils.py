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
        'Data Type': df.dtypes.astype(str).values,
        'Missing Values': df.isnull().sum().values,
        'Unique Values': df.nunique().values,
        'Sample Value': df.iloc[sample_row].values
    }, index=df.columns)

    data_dict.index.name = 'Column Name'
    return data_dict

def style_data_dictionary(df: pd.DataFrame) -> Styler:
    """Apply light style rules to a DataFrame. Intended for use with data dictionaries created by generate_data_dictionary().

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        Styler: A pandas Styler object.
    """
    styles = [
        dict(selector="th", props=[("font-size", "12px"), ("font-weight", "bold"), ("text-align", "left")]),
        dict(selector="td", props=[("font-size", "12px")])
    ]

    styled = df.style.set_table_styles(styles)
    return styled

def summarize_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize basic structural stats of a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: A summary with row count, column count, and attribute breakdown.
    """
    summary = {
        'Total Rows': len(df),
        'Total Columns': df.shape[1],
        'Numeric Columns': df.select_dtypes(include='number').shape[1],
        'Categorical Columns': df.select_dtypes(include='object').shape[1],
        'Datetime Columns': df.select_dtypes(include='datetime').shape[1],
        'Boolean Columns': df.select_dtypes(include='bool').shape[1],
        'Columns with Missing Values': df.isnull().any().sum()
    }

    return pd.DataFrame.from_dict(summary, orient='index', columns=['Value'])