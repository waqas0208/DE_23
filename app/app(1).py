# import sys
# # Prints the list of directories that the interpreter will search for the required module. 
# print(sys.path)
# import sys
# # Prints the list of directories that the interpreter will search for the required module. 
# print(sys.path)
import sqlite3
import pandas as pd
from flask import Flask, render_template
import sys
sys.path.append(r'C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2')

# Import the necessary functions for data processing
from data_ingestion.data_ingestion_abs_path import data_ingestion
from data_processing.data_processing_abs_path import data_processing
from data_aggregation.data_aggregation_abs_path import aggregate_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define the paths to the CSV file, database, and log file
csv_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2\data2ingest\financial_data.csv"
database_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2\db\financial_data.db"
log_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2\data_ingestion\data_ingestion.log"
# Perform data ingestion
data = data_ingestion(csv_file_path, database_file_path, log_file_path)

@app.route('/data_ingestion_results')
def data_ingestion_results():
    if data is None:
        return render_template('error.html', error_message="processed data not available.")
    # Convert DataFrame to a list of dictionaries
    ingested_data_list = data.to_dict(orient='records')

    return render_template('data_ingestion_results.html', ingested_data=ingested_data_list)


# Perform data processing
start_date = "2022-01-01"
end_date = "2022-01-02"
processed_data = data_processing(csv_file_path, database_file_path, start_date=start_date, end_date=end_date)

@app.route('/processed_data_results')
def processed_data_results():
    if processed_data is None:
        return render_template('error.html', error_message="processed data not available.")
    
    # Convert DataFrame to list of dictionaries
    processed_data_list = processed_data.to_dict(orient='records')
    
    return render_template('processed_data_results.html', processed_data=processed_data_list)

# Load the data from the database for aggregation
conn = sqlite3.connect(database_file_path)
aggregated_data = pd.read_sql_query("SELECT * FROM processed_data", conn)
conn.close()

@app.route('/data_aggregation_results')
def data_aggregation_results():
    if aggregated_data is None:
        return render_template('error.html', error_message="Aggregated data not available.")

    # Convert DataFrame to a list of dictionaries
    aggregated_data_list = aggregated_data.to_dict(orient='records')

    return render_template('data_aggregation_results.html', aggregated_data=aggregated_data_list)


if __name__ == '__main__':
    app.run(debug=True)
