import time
import logging
import pandas as pd
import os
import sqlite3

# Define file paths
csv_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2\data2ingest\financial_data.csv"
database_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2\db\financial_data.db"
log_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\DE\data2\data_aggregation\data_aggregation.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_file_path
)

def aggregate_data(data):
    """
    Perform data aggregation on the input data.
    
    Args:
        data (pandas.DataFrame): Input data for aggregation.
    
    Returns:
        pandas.DataFrame: Aggregated data.
    """
    logging.info("Step 3: Data Aggregation")
    start_time = time.time()
    try:
        aggregated_data = data.groupby('tstmp')['transaction_amount'].mean().reset_index()
        # Convert aggregated_data to DataFrame
        aggregated_data = pd.DataFrame(aggregated_data, columns=['tstmp', 'transaction_amount'])
        
        # Store aggregated data in the database
        conn = sqlite3.connect(database_file_path)
        aggregated_data.to_sql('aggregated_data', conn, if_exists='replace', index=False)
        conn.close()
        
        logging.info("Data aggregation successful. Number of rows in aggregated data: %d", len(aggregated_data))
        return aggregated_data
    except Exception as e:
        error_message = f"Error occurred during data aggregation: {str(e)}"
        logging.error(error_message)
        print("Data aggregation failed. Error:", str(e))
        raise e
    finally:
        end_time = time.time()
        logging.info(f"Time taken: {end_time - start_time} seconds")

# Test the data aggregation
if __name__ == "__main__":

    input_data = pd.DataFrame({
        'tstmp': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
        'transaction_amount': [100.0, 200.0, 150.0, 250.0]
    })
    
    aggregated_data = aggregate_data(input_data)
    print("Aggregated Data:")
    print(aggregated_data)
