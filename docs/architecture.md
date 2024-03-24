# Application's Architecture

In addressing the requirements outlined in this challenge, I've opted to employ a medallion architecture approach. Although the current solution is a preliminary rendition of this framework, featuring Raw, Structured, and Curated layers, it provides a structured methodology for managing data organization, transformation, and utilization. This approach prioritizes incremental improvements, adaptability, and governance, facilitating the exploration of advanced analytics and machine learning applications.

Here is a high-level architectural diagram illustrating the data flow journey, starting from API ingestion, progressing through the Raw, Structured, and ultimately Curated layers, before finally serving the data to downstream ML and Data Science teams.

### Target State Architecture
![Target Architecture](./img/architecture-diagram.png)

#### Raw Layer
In the code, I establish a connection to the API endpoint and retrieve the most recent data in JSON format. Upon obtaining the data, I augment it with two metadata attributes: `extract_time`, indicating the timestamp of the data extraction, and `source`, denoting the origin of the data, before writing this enriched JSON object into the raw layer. 

With each API call, a new JSON file is generated following the naming convention `raw_rates_{current_timestamp}.json`, where `{current_timestamp}` represents the timestamp of the current data extraction. This approach ensures that each dataset is uniquely identified and timestamped, facilitating traceability and versioning within the data pipeline.


![Raw json file](./img/raw.png)


#### Structured Layer
![Structured json file](./img/structured.png)


#### Curated Layer
![Curated json file](./img/curated.png)
