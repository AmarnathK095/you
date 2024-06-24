**YouTube Data Harvesting and Warehousing using SQL and Streamlit**

## **Introduction**
`          `YouTube Data Harvesting and Warehousing is a project that aims to allow users to access the data from multiple YouTube channels. The project utilizes SQL and Streamlit to create a user-friendly application that allows users to retrieve, store, and query YouTube channel and video data.
## **Project Overview**
`         `The YouTube Data Harvesting and Warehousing project consists of the following components:

- Streamlit Application: A user-friendly UI built using Streamlit library, allowing users to interact with the application and perform data retrieval and analysis tasks.
- YouTube API Integration: Integration with the YouTube API to fetch channel and video data based on the provided channel ID.
- SQL Data Warehouse: Migrate data into SQL server (MYSQL workbench), allowing for efficient querying and analysis using SQL queries.
## **Package need to import**
- import datetime
- from googleapiclient.discovery import build
- from IPython.display import JSON  
- import pandas as pd
- import mysql.connector


## **Technologies Used**
The following technologies are used in this project:

- Python: The programming language used for building the application and scripting tasks.
- Streamlit: A Python library used for creating interactive web applications and data visualizations.
- YouTube API: Google API is used to retrieve channel and video data from YouTube.
- MYSQL workbench: A relational database server used as a data warehouse for storing migrated YouTube data.
- Pandas: A data manipulation library used for data processing and analysis.
## **Installation and Setup**
To run the YouTube Data Harvesting and Warehousing project, follow these steps:

- Install Python: Install the Python programming language on your machine.
- Install Required Libraries: Install the necessary Python libraries using pip or conda package manager. Required libraries include Streamlit, MYSQL connector, Pandas.
- Set Up Google API: Set up a Google API project and obtain the necessary API credentials for accessing the YouTube API.
- Configure Database: Set up SQL database (MySQL workbench) for storing the data.
- Configure Application: Update the configuration file or environment variables with the necessary API credentials and database connection details.
- Run the Application: Launch the Streamlit application using the command-line interface.
## **Usage**
Once the project is setup and running, users can access the Streamlit application through a web browser. The application will provide a user interface where users can perform the following actions:

- Enter a YouTube channel ID to retrieve data for that channel.
- Store the retrieved data in the MYSQL workbench.
- Collect and store data for multiple YouTube channels in the workbench.
- Search and retrieve data from the SQL database using various search options.
- Perform data analysis and visualization using the provided features.

`       `**Features**

The YouTube Data Harvesting and Warehousing application offers the following features:

- Retrieval of channel and video data from YouTube using the YouTube API.
- Migrate data into SQL database for efficient querying and analysis.
- Search and retrieval of data from the SQL database using different search options, including joining tables
- Support for handling multiple YouTube channels and managing their data.

## **Conclusion**

The YouTube Data Harvesting and Warehousing project provides a powerful tool for retrieving, storing, and analyzing YouTube channel and video data. By leveraging SQL, MongoDB, and Streamlit, users can easily access and manipulate YouTube data in a user-friendly interface. The project offers flexibility, scalability, and data visualization capabilities, empowering users to gain insights from the vast amount of YouTube data available.

