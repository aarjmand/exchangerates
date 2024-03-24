### User's Guid

#### Introduction

This application was developed as part of a technical interview process during a recruitment drive. It serves as a comprehensive tool for curating exchange rates data from various API endpoints and delivering it to users for analytical purposes. The primary objectives of the development process were to fulfill the following requirements:

- Establish connectivity to any exchange rates API to retrieve data reflecting the exchange rates between Australia and New Zealand over the past 30 days, formatting it into JSON output.
- Implement preprocessing measures to address any anticipated data issues and ensure data quality.
- Conduct thorough data analysis, including identifying the best and worst exchange rates recorded within the specified time period, and calculating the average exchange rate for the month.

Additionally, the application incorporates a basic medallion architecture pattern and pipeline structure to enhance its coherence and efficiency.

#### Getting Started
The application has been developed using [JupyterLite](https://jupyter.org/try), with all source and test files stored in ```.ipynb``` format. To utilize the application, it is necessary to clone this repository into Jupyter or any other compatible platform.

Please ensure that all folders, except for the ```docs``` folder, are present in your environment for the application to function properly.

Once the setup is complete, navigate to the ```main.ipynb``` notebook and execute it. This process retrieves data from the API, organizes it into different layers, and generates a statistical table and two charts.

The statistical table and one of the charts offer interactive features, allowing users to select specific currencies for filtering purposes.


#### Using the Application

#### Troubleshooting
