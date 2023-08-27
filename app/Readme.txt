Data Processing and Aggregation Workflow using Flask
This repository contains a Flask web application that performs data processing and aggregation on financial data. The application allows users to ingest data from a CSV file, process it within a specified date range, and then perform aggregation on the processed data. The processed and aggregated results are displayed through different routes in the web application.

Prerequisites
Before running the application, make sure you have the following prerequisites installed:

Python (>= 3.6)
Flask
pandas
sqlite3
You can install the required Python packages using the following command:

pip install Flask pandas
Usage
Clone the repository to your local machine:


git clone https://github.com/yourusername/your-repo.git
Navigate to the repository directory:


cd your-repo
Modify the paths in the app.py file to point to your actual file locations:
python

csv_file_path = r"your_csv_file_path"
database_file_path = r"your_database_file_path"
log_file_path = r"your_log_file_path"
Run the Flask application:


python app.py
Open your web browser and navigate to http://localhost:5000 to access the web application.
Routes
The Flask application provides the following routes:

/: Home page with a basic welcome message.
/data_ingestion_results: Displays the ingested financial data.
/processed_data_results: Displays the processed financial data within the specified date range.
/data_aggregation_results: Displays the aggregated financial data.
Workflow Overview
Data Ingestion:
The data_ingestion function ingests data from a CSV file and stores it in an SQLite database. The ingested data is displayed on the /data_ingestion_results route.

Data Processing:
The data_processing function processes the data within a specified date range. Processed data is displayed on the /processed_data_results route.

Data Aggregation:
The aggregated data is obtained by querying the processed data from the database. Aggregated data is displayed on the /data_aggregation_results route.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.