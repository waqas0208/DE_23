import os
import pandas as pd
import logging
import sqlite3
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from sqlalchemy import create_engine, inspect


def create_preprocessed_table(database_path, preprocessed_data, table_name):
    """
    Create a table in the database and populate it with the preprocessed data.

    Args:
        database_path (str): Path to the database file.
        preprocessed_data (pandas.DataFrame): Preprocessed data.
        table_name (str): Name of the table to create.

    Returns:
        None
    """
    conn = None
    try:
        # Create a database connection
        conn = sqlite3.connect(database_path)
        # Save preprocessed data to the database
        preprocessed_data.to_sql(table_name, conn, if_exists='replace', index=False)

        conn.commit()

        logging.info(f"Table '{table_name}' created and populated successfully.")
    except Exception as e:
        error_message = f"Error occurred during table creation: {str(e)}"
        logging.error(error_message)
        raise e


def preprocess_data(data):
    print("Data before preprocessing:")
    print(data.head(10))

    # Remove duplicate entries
    data = data.drop_duplicates()

    # Label encode the account_number column
    label_encoder = LabelEncoder()
    data['account_number_encoded'] = label_encoder.fit_transform(data['account_number'])

    # Convert timestamp to Unix timestamp representation
    data['tstmp'] = data['tstmp'].apply(lambda x: datetime.timestamp(x))

    # Combine encoded columns with transaction_amount
    preprocessed_data = data[['transaction_amount', 'account_number_encoded', 'tstmp']]

    print("Data after preprocessing:")
    print(preprocessed_data.head(10))

    return preprocessed_data


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


def data_preprocessing(csv_file_path, database_path, start_date, end_date):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file_path)

    # Filter the data based on the specified date range
    data['tstmp'] = pd.to_datetime(data['tstmp'])
    data = data[(data['tstmp'] >= start_date) & (data['tstmp'] <= end_date)]

    # Perform the data preprocessing steps
    preprocessed_data = preprocess_data(data)

    # Create the preprocessed_data table in the database
    create_preprocessed_table(database_path, preprocessed_data, 'preprocessed_data')

    return preprocessed_data


def retrieve_data(database_path, table_name):
    """
    Retrieve data from a specified table in the SQLite database.

    Args:
        database_path (str): Path to the database file.
        table_name (str): Name of the table to retrieve data from.

    Returns:
        pandas.DataFrame: Retrieved data.
    """
    conn = sqlite3.connect(database_path)
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data


def retrieve_table_names(database_path):
    """
    Retrieve the table names from the SQLite database.

    Args:
        database_path (str): Path to the database file.

    Returns:
        list: List of table names in the database.
    """
    engine = create_engine(f'sqlite:///{database_path}')
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    engine.dispose()
    return table_names


if __name__ == "__main__":
    # Determine the base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Set up logging
    log_file_path = os.path.join(base_dir, "2_data_preprocessing.log")
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    csv_file_path = os.path.join(base_dir, "financial_data.csv")
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 3, 31)

    # Create the database
    database_file_path = os.path.join(base_dir, "financial_data.db")
    create_database(database_file_path)

    # Perform data preprocessing
    preprocessed_data = data_preprocessing(csv_file_path, database_file_path, start_date, end_date)

    # Retrieve and print the preprocessed data
    retrieved_data = retrieve_data(database_file_path, "preprocessed_data")
    print("Preprocessed Data:")
    print(retrieved_data)

    # Retrieve and print the table names
    table_names = retrieve_table_names(database_file_path)
    print("Table Names:")
    print(table_names)
