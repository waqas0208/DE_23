# Use an official SQLite image as the base image
FROM sqlite:latest

# Copy the database file to the container
COPY financial_data.db /data2/
COPY requirements.txt app

# Specify the working directory
WORKDIR /data2

# Expose the port (if needed)
# EXPOSE 5432

# Define the command to run when the container starts
CMD ["sqlite3", "financial_data.db"]
