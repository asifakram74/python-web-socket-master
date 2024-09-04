# Use the official Python image from the Docker Hub
FROM python:3.11-slim


# Set environment variables to improve Python behavior in Docker
# Prevent Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure that Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies
# Copy the requirements file into the container
COPY requirements.txt /app/
# Upgrade pip to the latest version
RUN pip install --upgrade pip
# Install the dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Install Daphne for running the ASGI application
RUN pip install daphne

# Copy the entire project into the container's work directory
COPY . /app/

# Optionally collect static files (uncomment if necessary in production)
# RUN python manage.py collectstatic --noinput

# Expose the port on which the Django app will run
EXPOSE 8000

# Run the Daphne server to serve the Django ASGI application
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "sync_hub.asgi:application"]
