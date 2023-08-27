# Import statements
BATCH_SIZE = 10000  # Set your desired batch size
# Definitions of functions like create_processed_table, process_data, create_database, etc.
# The new process_data_batch function here
def process_data_batch(batch_data):
    # Similar to process_data function, but applied to a batch
    batch_data = batch_data.drop_duplicates()
    label_encoder = LabelEncoder()
    batch_data['account_number_encoded'] = label_encoder.fit_transform(batch_data['account_number'])
    batch_data['tstmp'] = batch_data['tstmp'].apply(lambda x: datetime.timestamp(x))
    processed_data = batch_data[['transaction_amount', 'account_number_encoded', 'tstmp']]
    return processed_data
def process_large_data(data):
    num_batches = len(data) // BATCH_SIZE + 1
    processed_batches = []

    for batch_num in range(num_batches):
        start_idx = batch_num * BATCH_SIZE
        end_idx = (batch_num + 1) * BATCH_SIZE
        batch_data = data[start_idx:end_idx]
        processed_batch = process_data_batch(batch_data)
        processed_batches.append(processed_batch)

    return pd.concat(processed_batches, ignore_index=True)
def process_data_batch(batch_data):
    # ...
def process_large_data(data):
    # ...
if __name__ == "__main__":
    # Define file paths
    log_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\data_processing\data_processing.log"
    csv_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\data\financial_data.csv"
    database_file_path = r"C:\Users\waqas\OneDrive - IU International University of Applied Sciences\Dokumente\MSc Data Science\WS22-23\Portfolio\data2\db\financial_data.db"

    # Set up logging
    logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Create the database
    create_database(database_file_path)

    # Define date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 3, 31)

    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file_path)

    # Filter the data based on the specified date range
    data['tstmp'] = pd.to_datetime(data['tstmp'])
    data = data[(data['tstmp'] >= start_date) & (data['tstmp'] <= end_date)]

    # Perform data processing in batches
    processed_data = process_large_data(data)
    create_processed_table(database_file_path, processed_data, 'processed_data')

    # Retrieve and print the processed data
    retrieved_data = retrieve_data(database_file_path, "processed_data")
    print("processed Data:")
    print(retrieved_data)

    # Retrieve and print the table names
    table_names = retrieve_table_names(database_file_path)
    print("Table Names:")
    print(table_names)