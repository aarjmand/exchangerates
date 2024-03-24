### User's Guide

### Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)

#### Introduction

This application was developed as part of a technical interview process during a recruitment drive. It serves as a comprehensive tool for curating exchange rates data from various API endpoints and delivering it to users for analytical purposes. The primary objectives of the development process were to fulfill the following requirements:

- Establish connectivity to any exchange rates API to retrieve data reflecting the exchange rates between Australia and New Zealand over the past 30 days, formatting it into JSON output.
- Implement preprocessing measures to address any anticipated data issues and ensure data quality.
- Conduct thorough data analysis, including identifying the best and worst exchange rates recorded within the specified time period, and calculating the average exchange rate for the month.

Additionally, the application incorporates a basic medallion architecture pattern and pipeline structure to enhance its coherence and efficiency.

#### Getting Started

##### Environment Setup
The application has been developed using [JupyterLite](https://jupyter.org/try), with all source and test files stored in ```.ipynb``` format. To utilize the application, it is necessary to clone this repository into Jupyter or any other compatible platform.

Please ensure that all folders, except for the ```docs``` folder, are present in your environment for the application to function properly. You can access the comprehensive folder structure of the application in the [Appendix](#appendix) section of this document.

Once the setup is complete, navigate to the ```main.ipynb``` notebook and execute it. This process retrieves data from the API, organizes it into ```Raw```, ```Structured``` & ```Curated``` layers, and generates a statistical table and two charts.

The statistical table and one of the charts offer interactive features, allowing users to select specific currencies for filtering purposes.

##### Configuration Settings
This is where I put config settigns

#### Using the Application

#### Troubleshooting

#### Appendix

```
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
