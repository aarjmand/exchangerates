import sys
import pandas as pd
import matplotlib.pyplot as plt
from helpers import *

_config = None
_logger = None

def main():

    endpoint = build_endpoint(_config)

    data = get_data(endpoint)

    flat_rates = [(date, currency, rate) for date, currencies in data['rates'].items() for currency, rate in currencies.items()]
    df = pd.DataFrame(flat_rates, columns=['Date', 'Currency', 'Rate'])

    rs = df.groupby(['Currency']).agg(
        mean=('Rate', 'mean'),
        worst=('Rate', 'min'),
        best=('Rate', 'max')
    )

    print(rs)

if __name__ == "__main__":
    _config = load_config('../conf/config.ini')
    _logger = get_logger()

    try:
        _logger.info('Initializing the app!')
        main()
    except Exception as e:
        _logger.exception(f"An error occured: {str(e)}")
        sys.exit(1)
