# ExchangeRates

As part of Bupa's recruitment process, candidates are tasked with a Python coding challenge. The challenge involves retrieving exchange rate data between Australia and New Zealand from the past 30 days using any available exchange rates API and performing comprehensive analysis on the dataset.

This repository is dedicated to showcasing my solution to the coding challenge for the recruitment team at Bupa.

Below are the key requirments for this coding challenge;

- Connect to any exchange rates API to get exchange rates of Australia to New Zealand for the past 30 days into JSON output format.
- Pre-process the data to manage any expected issues.
- Perform some data analysis.
- Find the best and worst exchange rates for that time period.
- Calculate the average exchange rate for the month.

### Docs

Information regarding the application's architecture can be explored [here](https://github.com/aarjmand/exchangerates/tree/main/docs/architecture.md). 

### Project Structure

```bash
exchangerates/
├── conf/
│   ├── config.ini
|   └── logging.conf
|
|── data/
|   ├── curated/
|   |   └── summary_rates.json
|   |
|   │── raw/
|   │   ├── raw_rates_2024-03-23 23_28_59.799000.json
|   |   └── raw_rates_2024-03-23 23_29_45.542000.json
|   |
│   └── structured/
|       └── structured_rates.json
|
|── docs/
|    └── architecture.md
|
|── logs/
|   └── exchangerates.log
|
|── notebooks/
|   │── src/
|   │   │── analytics.ipynb
|   │   │── helpers.ipynb
|   │   │── main.ipynb
|   │   └── pipeline.ipynb
|   |
|   └── tests/
|       └── test_module2.py
|       └── test_module2.py
|
├── LICENSE
└── README.md
 
```
