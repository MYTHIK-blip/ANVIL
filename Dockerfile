# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install .[dev]

# Copy the rest of the application's code
COPY . .

# Command to keep the container running for development
CMD ["tail", "-f", "/dev/null"]
