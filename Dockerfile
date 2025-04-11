# Use an official Python runtime as a parent image
FROM python:alpine3.20
# Set environment variables to prevent Python from writing .pyc files and to ensure output is flushed immediately

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn redis

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]