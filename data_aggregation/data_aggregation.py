import time
import logging
import pandas as pd
import sqlite3

def retrieve_data(database_file_path, table_name):
    """
    Retrieve data from a specified table in the SQLite database.

    Args:
        database_file_path (str): Path to the database file.
        table_name (str): Name of the table to retrieve data from.

    Returns:
        pandas.DataFrame: Retrieved data.
    """
    conn = sqlite3.connect(database_file_path)
    query = f"SELECT * FROM {table_name}"
    print("Executing query:", query)
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def aggregate_data_from_processed(data, conn):
    """
    Perform data aggregation on the processed data.

    Args:
        data (pandas.DataFrame): Processed data for aggregation.
        conn (sqlite3.Connection): Connection to the SQLite database.

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
        aggregated_data.to_sql('aggregated_data', conn, if_exists='replace', index=False)
        
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

if __name__ == "__main__":
    # Define file paths
    log_path = './data_processing.log'
    database_file_path = './financial_data.db'

    # Set up logging
    logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Define table name
    table_name = "processed_data"

    # Retrieve and print the processed data
    retrieved_data = retrieve_data(database_file_path, table_name)
    print("processed Data:")
    print(retrieved_data)

    # Connect to the database
    conn = sqlite3.connect(database_file_path)

    # Perform data aggregation
    aggregated_data = aggregate_data_from_processed(retrieved_data, conn)
    print("Aggregated Data:")
    print(aggregated_data)

    # Close the connection
    conn.close()
