import os
import pandas as pd
import logging
import sqlite3

def data_ingestion(file_path, database_path):
    """
    Perform data ingestion from a CSV file and store it in a database.

    Args:
        file_path (str): Path to the CSV file.
        database_path (str): Path to the database file.

    Returns:
        pandas.DataFrame: The ingested data as a DataFrame.
    """
    try:
        # Create a database connection
        conn = create_database(database_path)

        # Determine the base directory
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute file path
        absolute_file_path = os.path.join(base_dir, file_path)

        # Perform data ingestion
        data = pd.read_csv(absolute_file_path)
        data.to_sql("financial_data", conn, if_exists="replace")

        logging.info("Data ingestion successful. Number of rows: %d", len(data))

        return data.head(10)
    except Exception as e:
        error_message = f"Error occurred during data ingestion: {str(e)}"
        logging.error(error_message)
        raise e
    finally:
        if conn:
            conn.close()

def create_database(database_path):
    """
    Create a new SQLite database.

    Args:
        database_path (str): Path to the database file.

    Returns:
        sqlite3.Connection: Connection object for the database.
    """
    try:
        # Create a database connection
        conn = sqlite3.connect(database_path)

        logging.info("Database created successfully.")

        return conn
    except Exception as e:
        error_message = f"Error occurred during database creation: {str(e)}"
        logging.error(error_message)
        raise e

if __name__ == "__main__":
    # Determine the base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Set up logging
    log_file_path = os.path.join(base_dir, "1_data_ingestion.log")
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    csv_file_path = "financial_data.csv"
    database_file_path = os.path.join(base_dir, "financial_data.db")

    print(data_ingestion(csv_file_path, database_file_path))
