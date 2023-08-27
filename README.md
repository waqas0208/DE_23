# DE_23


# Financial Data Processing Project

This repository contains a comprehensive financial data processing project with modules for data ingestion, processing, and aggregation. The project is structured into different modules, each designed to handle a specific stage of the data pipeline. Additionally, a web application is included to interactively display and visualize the processed data.

## Project Structure

The repository is structured as follows:

* **app** : Contains the Flask web application files, including templates for rendering HTML pages and the main `app.py` script.
* **data_ingestion** : Handles data ingestion from a CSV file and stores it in an SQLite database. The module includes the `data_ingestion.py` script, `financial_data.csv` for testing, and a `data_ingestion.log` for logging.
* **data_processing** : Performs data processing on input data, including deduplication, label encoding, and timestamp conversion. The module includes the `data_processing.py` script, `preprocessed_data.csv` for testing, and a `data_processing.log` for logging.
* **data_aggregation** : Performs data aggregation on processed data and stores aggregated results in the database. The module includes the `data_aggregation.py` script, `aggregated_data.csv` for testing, and a `data_aggregation.log` for logging.
* **db** : Contains the SQLite database file `financial_data.db`.
* **data** : Holds the original `financial_data.csv` file.
* **.gitignore** : Specifies files and directories to be ignored by Git.
* **README.md** : The main project overview document you are currently reading.
* **CONTRIBUTING.md** : Guidelines for potential contributors to the project.
* **LICENSE** : The chosen open-source license for the project.

## Usage

### Data Ingestion Module

For information on how to use the data ingestion module, refer to the [data_ingestion README](https://chat.openai.com/data_ingestion/README.md).

### Data Processing Module

For information on how to use the data processing module, refer to the [data_processing README](https://chat.openai.com/data_processing/README.md).

### Data Aggregation Module

For information on how to use the data aggregation module, refer to the [data_aggregation README](https://chat.openai.com/data_aggregation/README.md).

### Web Application

The Flask web application provides an interactive way to visualize the processed and aggregated data. The templates for rendering HTML pages are located in the `app/templates` directory, while the `app/static` directory holds static assets like CSS, JavaScript, and images.

To run the web application, execute the `app.py` script within the `app` directory. Access the application by opening a web browser and navigating to `http://localhost:5000`.

## Contributing

Contributions to this project are welcome! Please refer to the [CONTRIBUTING.md](https://chat.openai.com/CONTRIBUTING.md) document for guidelines on how to contribute.

## License

This project is licensed under the terms of the [MIT License](https://chat.openai.com/LICENSE).
