import logging
import sqlite3
from flask import Flask, render_template
import sys

# Append module directories to sys.path
sys.path.append(r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\data_ingestion")
sys.path.append(r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\data_processing")
sys.path.append(r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\data_aggregation")

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration settings (import from config.py if applicable)
CSV_FILE_PATH = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\data\financial_data.csv"
DATABASE_FILE_PATH = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\db\financial_data.db"


def get_data_ingestion():
    # Import the necessary functions for data ingestion
    from data_ingestion import data_ingestion
    log_file_path = './data_ingestion.log'
    return data_ingestion(CSV_FILE_PATH, DATABASE_FILE_PATH, log_file_path)


def get_processed_data(start_date, end_date):
    # Import the necessary functions for data processing
    from data_processing import data_processing
    return data_processing(CSV_FILE_PATH, DATABASE_FILE_PATH, start_date=start_date, end_date=end_date)

def get_aggregated_data():
    # Import the necessary functions for data aggregation
    from data_aggregation import aggregate_data_from_processed

    # Define the start and end dates
    start_date = "2022-01-01"
    end_date = "2022-01-02"

    # Get the processed data for aggregation
    data = get_processed_data(start_date, end_date)

    # Create a SQLite database connection
    conn = sqlite3.connect(DATABASE_FILE_PATH)

    try:
        # Perform data aggregation using the imported function and provide the database connection
        aggregated_data = aggregate_data_from_processed(data, conn)

        return aggregated_data
    finally:
        # Close the database connection
        conn.close()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data_ingestion_results')
def data_ingestion_results():
    data = get_data_ingestion()
    if data is None:
        return render_template('error.html', error_message="Processed data not available.")
    ingested_data_list = data.to_dict(orient='records')
    return render_template('data_ingestion_results.html', ingested_data=ingested_data_list)

@app.route('/processed_data_results')
def processed_data_results():
    start_date = "2022-01-01"
    end_date = "2022-01-02"
    processed_data = get_processed_data(start_date, end_date)
    if processed_data is None:
        return render_template('error.html', error_message="Processed data not available.")
    processed_data_list = processed_data.to_dict(orient='records')
    return render_template('processed_data_results.html', processed_data=processed_data_list)

@app.route('/data_aggregation_results')
def data_aggregation_results():
    aggregated_data = get_aggregated_data()
    if aggregated_data is None:
        return render_template('error.html', error_message="Aggregated data not available.")
    aggregated_data_list = aggregated_data.to_dict(orient='records')
    return render_template('data_aggregation_results.html', aggregated_data=aggregated_data_list)

if __name__ == '__main__':
    app.run(debug=True)
