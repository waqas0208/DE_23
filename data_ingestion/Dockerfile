# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /data2

# Copy the CSV file and the database file to the container
COPY financial_data.csv .
COPY data_ingestion.py .
COPY requirements.txt .
COPY data_ingestion.log .

#run requirements for modules
RUN pip install pandas

# Expose port 5000 (or any other port your Flask app is listening on)
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["python", "data_ingestion.py"]
