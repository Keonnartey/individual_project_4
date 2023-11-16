## DataBricks ETL Pipeline [![CI](https://github.com/Keonnartey/databricks_project/actions/workflows/ci.yml/badge.svg)](https://github.com/Keonnartey/databricks_project/actions/workflows/ci.yml)


### Introduction
This project develops a Databricks ETL(Extract, Transform, Load) Pipeline for retrieving and processing `Spotify Songs`, featuring a well-documented notebook for ETL operations, Delta Lake for storage, Spark SQL for transformations, and data visualizations for actionable insights.
It ensures data integrity through robust error handling and data validation. 
An automated Databricks API trigger highlights the focus on automation and continuous processing.

This workflow includes running a Makefile to for specific installation for `testing`, `formatting`, `linting` using Github Actions. This automation streamlines the data analysis process and enhances code quality.

### Data Preparation

I used the [Spotify Dataset](https://gist.githubusercontent.com/rioto9858/ff72b72b3bf5754d29dd1ebf898fc893/raw/1164a139a780b0826faef36c865da65f2d3573e0/top50MusicFrom2010-2019.csv) with several columns and information such as title of songs, artist, year song was released, genre of the songs, the tempo of the songs, energy of the songs, danceability, loudness, liveness, popularity of the songs from 2010 - 2019

### Databricks Installations and Environment Setup

- Create a Databricks workspace on Azure
- Connect GitHub account to Databricks Workspace
- Create global init script for cluster start to store environment variables
- Establishes a connection to the Databricks environment using environment variables for authentication (SERVER_HOSTNAME and ACCESS_TOKEN).
- Create a Databricks cluster that supports Pyspark
- Clone Github repo into Databricks workspace
- Create a job on Databricks to build an ETL pipeline

### Usage and Functionality

main.py: imports functions from three different modules: `extract` from the mylib.extract module, `load` from the mylib.transform module, and both `query_transform` and `show_plot()` from the mylib.query_viz module.

(1) Data Extraction mylib/extract.py:

Environment Setup: loads environment variables using dotenv, includes the server hostname and access token necessary for API authentication.
Utilizes the `requests` library to fetch airline safety data from specified URLs.
- API Communication Functions: defines several functions to interact with the Databricks REST API:
- perform_query: Makes API requests and returns the response in JSON format.
- mkdirs: Creates directories in Databricks FileStore.
- create: Initializes file creation in the FileStore.
- add_block: Adds a block of data to a file in the FileStore.
- close: Closes the file operation.
- File Upload Process: The put_file_from_url function downloads a file from a given URL and uploads it to the Databricks FileStore, handling the data in blocks and encoding it in base64 format. It also ensures that files are overwritten if specified.
- extract: First ensures the target directory exists, then downloads and stores the data in the Databricks FileStore.

(2) Data Transformation and Load mylib/transform_load.py:

- load: Transform the csv file into a Spark dataframe which is then converted into a Delta Lake Table `top50musicfrom2010_2019_delta` and stored in the Databricks environment.

(3) Query Transformation and Visualization mylib/query_viz.py:

- Defines a Spark SQL query to perform a predefined transformation on the retrieved data.
- Also produces a simple bar plot to show some visualisations and results.

This Query checks for how many times famous Pop star Rihanna appears in the dataset and creates a simple bar plot to showcase this visually.
  
![histogram_plot](https://github.com/Keonnartey/databricks_project/assets/125210401/2583ad2b-30c0-4c04-8b51-4e6cc0fbdc6b)

#### Databricks Pipeline and Jobs

<img width="1280" alt="Screenshot 2023-11-15 at 7 27 44 PM" src="https://github.com/Keonnartey/databricks_project/assets/125210401/bd6ee0cb-d1eb-498d-8072-86008452825e">

<img width="1440" alt="Screenshot 2023-11-15 at 11 02 29 PM" src="https://github.com/Keonnartey/databricks_project/assets/125210401/bc73db63-5248-46f7-a3e1-4a30d0d33f3b">


#### References

https://github.com/nogibjj/python-ruff-template
https://hypercodelab.com/docs/spark/databricks-platform/global-env-variables/
https://docs.databricks.com/en/dbfs/filestore.html
https://learn.microsoft.com/en-us/azure/databricks/delta/
https://docs.databricks.com/en/getting-started/data-pipeline-get-started.html

