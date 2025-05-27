# Use an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all necessary Python scripts into the container
COPY main.py geohospital.py .

# Set the default command to run the main script
CMD ["python", "main.py"]
