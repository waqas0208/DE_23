# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script to the container
COPY data_aggregation_abs_path.py /app/
COPY requirements.txt app

# Install pandas and sqlite3 (required dependencies)
RUN pip install pandas

# Run the script when the container launches
CMD ["python", "data_aggregation_abs_path.py"]
