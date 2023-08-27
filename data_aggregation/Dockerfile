# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /data2

# Copy the microservice files and requirements to the container
COPY data_aggregation.py .
COPY requirements.txt .
COPY financial_data.db .


# Install required dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the microservice when the container launches
CMD ["python", "data_aggregation.py"]
