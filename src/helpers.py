import requests
import logging
import logging.config
import configparser
from datetime import datetime, timedelta

def get_logger():
    """

    Initializes a logger object based on specified configurations

    Parameters:
    No parameters are passed into this function.

    Returns:
    logger: A logger object.
    """
    logging.config.fileConfig('../conf/logging.conf')
    logger = logging.getLogger('exchangerates')

    return logger

def get_data(url):
    """

    Fetches data from an specified endpoint.

    Parameters:
    url (str): The URL endpoint to fetch data from.

    Returns:
    dict: The JSON data fetched from the endpoint.
    """
    response = requests.get(url, timeout=15)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    return response.json()

def load_config(config_file):
    """

    Loads application configuration file.

    Parameters:
    config_file (str): Path to the configuration file.

    Returns:
    ConfigParser: An object of type ConfigParser
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    return config

def get_start_date(date_threshold):
    """

    Calculates a date based on a date threshold value.

    Parameters:
    date_threshold (int): Number of dates to deduct from current date.

    Returns:
    date: An object of type Date.
    """
    return datetime.now().date() - timedelta(days=date_threshold)

def get_current_date():
    """

    Get the current date of the system.

    Parameters:
    No parameters are passed into this function.

    Returns:
    date: An object of type Date.
    """
    return datetime.now().date()

def build_endpoint(config):
    """

    Builds an endpoint based on values in the configuration file.

    Parameters:
    config (ConfigParser): Number of dates to deduct from current date.
    
    Returns:
    str: A complete endpoin
    """
    config_section  = dict(config.items('arguments'))

    url = config_section['endpoint']
    access_key = config_section['access_key']
    start_date = get_start_date(int(config_section['date_threshold']))
    end_date = get_current_date()
    base_currency = config_section['base_currency']
    symbols = config_section['symbols']

    return f"{url}?access_key={access_key}&start_date={start_date}&end_date={end_date}&base={base_currency}&symbols={symbols}"