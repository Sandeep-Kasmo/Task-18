📘 Project: SharePoint Metadata Extraction & ETL Pipeline

This project implements a lightweight ETL (Extract–Transform–Load) workflow for retrieving project metadata from a SharePoint site, processing it, and preparing it for downstream reporting or analytics systems. The pipeline is modular, configurable, and designed to run both locally and within automated job environments.

📁 Folder Structure

                SHAREPOINT/
                │
                ├── config/
                │   └── config.ini              # Configuration: SharePoint URLs, credentials, file paths
                │
                ├── src/
                │   ├── config_loader.py        # Utility to parse and load config.ini settings
                │   ├── extract.py              # Extract step: connects to SharePoint and fetches metadata
                │   ├── transform.py            # Transform step: cleans, validates, and shapes the data
                │   └── load.py                 # Load step: outputs CSV, DB insert, or other targets
                │
                ├── main.py                     # Pipeline orchestrator combining Extract → Transform → Load
                ├── requirements.txt            # Python dependencies for the entire project
                └── .gitignore                  # Version control exclusions

🎯 Objective

The goal of this project is to collect project-related metadata stored in a SharePoint list or document library and prepare it for management dashboards, status reporting, or integration with enterprise data systems.

The workflow:

Connects to a SharePoint site using configured authentication.

Retrieves metadata files or list entries.

Loads the results into memory for cleaning and transformation.

Outputs standardized datasets for analytics or storage.

🔧 Features

Config-driven SharePoint connection settings

Modular ETL components (extraction, transformation, loading)

Ability to read remote metadata stored as CSV, JSON, or list records

Structured data validation before transforming

Support for saving results locally or forwarding to a database

Clean and maintainable architecture suitable for extensions

🚀 Getting Started

1. Install dependencies

                pip install -r requirements.txt

2. Configure SharePoint settings

Edit the file:

                config/config.ini


Provide:

SharePoint site URL

Authentication method

Path to the metadata file or list

Output destination

3. Run the pipeline

Run the entire ETL:

                python main.py


Or run each step individually:

                python src/extract.py
                python src/transform.py
                python src/load.py

📥 Extract Step

extract.py retrieves metadata from SharePoint using credentials and paths defined in config.ini.
The script loads the file into memory and returns it as a Pandas DataFrame for downstream processing.

🔄 Transform Step

transform.py performs:

Cleaning

Standardizing columns

Validating required fields

Applying business rules

Preparing structured output

All transformations are designed to be reusable and extendable.

📤 Load Step

load.py handles final output:

Save to local CSV

Insert into a database

Forward to an API

Provide data artifacts for reporting

The loading logic can be customized as needed.

🧩 Extensibility

This project can be expanded with:

Automated scheduling (Airflow, Cron, Azure Automation)

Additional data sources

Enhanced SharePoint authentication modes

Data quality checks

Cloud deployment pipelines

📄 License


This project can be adapted and used freely within your organization.
