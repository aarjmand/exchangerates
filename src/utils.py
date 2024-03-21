import requests
import logging
import logging.config
import pandas as pd

def get_logger():
    """

    Initializes a logger object based on specified configurations

    Parameters:
    No parameters are passed into this function

    Returns:
    logger: A logger object
    """
    logging.config.fileConfig('../conf/logging.conf')
    logger = logging.getLogger('exchangerates')

    return logger

def get_data(url: str):
    """

    Fetches data from the specified URL.

    Parameters:
    url (str): The URL to fetch data from.

    Returns:
    dict: The JSON data fetched from the URL.
    """
    response = requests.get(url, timeout=15)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    return response.json()

