import pandas as pd
import logging
import sqlite3

def data_ingestion(csv_file_path, database_file_path, log_file_path):
    """
    Perform data ingestion from a CSV file and store it in a database.

    Args:
        csv_file_path (str): Absolute path to the CSV file.
        database_file_path (str): Absolute path to the database file.
        log_file_path (str): Absolute path to the log file.

    Returns:
        pandas.DataFrame: The ingested data as a DataFrame.
    """
    try:
        # Set up logging
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

        # Perform data ingestion
        data = pd.read_csv(csv_file_path)

        # Use context manager to open and close the database connection
        with create_database(database_file_path) as conn:
            data.to_sql("financial_data", conn, if_exists="replace")

        logging.info("Data ingestion successful. Number of rows: %d", len(data))

        return data.head(100)
    except Exception as e:
        error_message = f"Error occurred during data ingestion: {str(e)}"
        logging.error(error_message)
        raise e

def create_database(database_file_path):
    """
    Create a new SQLite database.

    Args:
        database_file_path (str): Absolute path to the database file.

    Returns:
        sqlite3.Connection: Connection object for the database.
    """
    try:
        # Create a database connection
        conn = sqlite3.connect(database_file_path)

        logging.info("Database created successfully.")

        return conn
    except Exception as e:
        error_message = f"Error occurred during database creation: {str(e)}"
        logging.error(error_message)
        raise e
 
if __name__ == "__main__":
    # Define the path to the CSV file within the Docker container
    csv_file_path = './financial_data.csv'

    # Define absolute paths for database and log file within the container
    database_file_path = './financial_data.db'
    log_file_path = './data_ingestion.log'

    print(data_ingestion(csv_file_path, database_file_path, log_file_path))



