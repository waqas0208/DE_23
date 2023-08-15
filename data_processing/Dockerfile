# Use the official Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script and other necessary files to the container
COPY data_processing_abs_path.py /app/
COPY financial_data.csv /app/
COPY financial_data.db /app/
COPY requirements.txt app

# Install required dependencies
RUN pip install pandas scikit-learn sqlalchemy

# Run the script
CMD ["python", "data_processing_abs_path.py"]
