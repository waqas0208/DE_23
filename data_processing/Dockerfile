# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /data2

# Copy the script and other necessary files to the container
COPY data_processing.py .
COPY requirements.txt .
COPY financial_data.csv .
COPY financial_data.db .

# Install required dependencies
RUN pip install pandas scikit-learn sqlalchemy

# Expose port 5000 (or any other port your Flask app is listening on)
EXPOSE 5000

# Run the script
CMD ["python", "data_processing.py"]
