import sys
from helpers import *

_config = None
_logger = None

def main():

    endpoint = build_endpoint(_config)
    print(endpoint)

if __name__ == "__main__":
    _config = load_config('../conf/config.ini')
    _logger = get_logger()

    try:
        main()
    except Exception as e:
        _logger(f"An error occured: {str(e)}")
        sys.exit(1)
