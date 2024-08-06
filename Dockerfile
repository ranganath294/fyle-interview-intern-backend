# Use Python 3.8 slim runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=core/server.py

# Expose the port the app runs on
EXPOSE 7755

# Command to start the server using a bash script
CMD ["bash", "run.sh"]
