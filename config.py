import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(key: str) -> str:
    """Pull value from .env based on provided key.

    Args:
        key (string): key to key-value pair in .env.

    Returns:
        string: the value from .env.

    Raises:
        EnvironmentError: If key is not present in .env.
    """
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Environment variable '{key}' is not set.")
    return value

def validate_path(path: str) -> str:
    """Determine if a provided filepath is valid.

    Args:
        path (string): filepath to be checked.

    Returns:
        path: valid filepath.

    Raises:
        FileNotFoundError: If path cannot be resolved.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found at {path}")
    return path

# Validated paths
LENDING_CLUB_ACCEPTED = validate_path(get_env_var('LENDING_CLUB_ACCEPTED'))
LENDING_CLUB_REJECTED = validate_path(get_env_var('LENDING_CLUB_REJECTED'))