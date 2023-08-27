# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /data2

# Copy the Flask app files to the container
COPY app.py .
COPY templates templates .
COPY static static .
COPY financial_data.csv .
COPY data_ingestion.py .
COPY requirements.txt .
COPY data_ingestion.log .
COPY data_ingestion.py .
COPY data_processing.py .
COPY data_aggregation.py .

# Install required dependencies
RUN pip install -r requirements.txt

# Expose port 5000 (or any other port your Flask app is listening on)
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["python", "app.py"]
