# Use an official SQLite image as the base image
FROM alpine:latest

# Install SQLite
RUN apk add --no-cache sqlite

# Create a directory for the database file
RUN mkdir /data

# Copy the financial_data.db file to the /data directory in the container
COPY financial_data.db /data/

# Set the working directory to /data
WORKDIR /data
