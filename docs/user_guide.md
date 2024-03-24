# User's Guide

### Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Environment Setup](#environment-setup)
  - [Configuration Settings](#configuration-settings)
- [Using the Application](#using-the-application)
- [Troubleshooting](#troubleshooting)
- [Appendix](#appendix)

### Introduction

This application was developed as part of a technical interview process during a recruitment drive. It serves as a comprehensive tool for curating exchange rates data from various API endpoints and delivering it to users for analytical purposes. The primary objectives of the development process were to fulfill the following requirements:

- Establish connectivity to any exchange rates API to retrieve data reflecting the exchange rates between Australia and New Zealand over the past 30 days, formatting it into JSON output.
- Implement preprocessing measures to address any anticipated data issues and ensure data quality.
- Conduct thorough data analysis, including identifying the best and worst exchange rates recorded within the specified time period, and calculating the average exchange rate for the month.

Additionally, the application incorporates a basic medallion architecture pattern and pipeline structure to enhance its coherence and efficiency.

### Getting Started

#### Environment Setup

The application has been developed using [JupyterLite](https://jupyter.org/try), with all source and test files stored in ```.ipynb``` format. To utilize the application, it is necessary to clone this repository into Jupyter or any other compatible platform.

Please ensure that all folders, except for the ```docs``` folder, are present in your environment for the application to function properly. You can access the comprehensive folder structure of the application in the [Appendix](#appendix) section of this document.

Once the setup is complete, navigate to the ```main.ipynb``` notebook and execute it. This process retrieves data from the API, organizes it into ```Raw```, ```Structured``` & ```Curated``` layers, and generates a statistical table and two charts.

The statistical table and one of the charts offer interactive features, allowing users to select specific currencies for filtering purposes.

#### Configuration Settings

The application does not accept user-supplied parameters directly. However, users can configure specific attributes by editing the ```config.ini``` file provided with the application. This file contains some default values as can be seen in the table bellow, but for a more comprehensive description and allowd list of values for each attribute consult the [Appendix](#appendix) section of this document.

```python
[arguments]
endpoint=https://api.exchangeratesapi.io/v1/timeseries
access_key=26e5547f91c8fd04634605e604ce5835
date_threshold=30
base_currency=AUD
symbols=NZD,USD,GBP,EUR,COP,ARS,DOP
```



### Using the Application

### Error Handling

### Appendix

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
