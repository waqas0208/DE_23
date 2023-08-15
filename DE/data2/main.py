import pandas as pd
import logging
import time

def data_ingestion():
    # Configure logging
    logging.basicConfig(filename=r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio DE\Data\data_log.log", level=logging.INFO)

    # Step 1: Data Ingestion
    logging.info("Step 1: Data Ingestion")
    start_time = time.time()
    try:
        data = pd.read_csv(r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio DE\Data\financial_data.csv")
        print("Data ingestion successful. Number of rows:", len(data))
    except Exception as e:
        error_message = f"Error occurred during data ingestion: {str(e)}"
        logging.error(error_message)
        print("Data ingestion failed. Error:", str(e))
        raise e
    end_time = time.time()
    logging.info(f"Time taken: {end_time - start_time} seconds")

    return data

# Import the data_ingestion function from the same file
from main import data_ingestion

# Call the data_ingestion function
data = data_ingestion()
