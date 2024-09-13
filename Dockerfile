# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8081 for the Flask application
EXPOSE 8081

# Define environment variable
ENV FLASK_APP=helloworld.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8081"]
