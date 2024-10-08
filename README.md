## Sync Hub - Dockerized Django Backend

This section provides instructions on how to set up and run the Django backend for the `sync_hub` project using Docker.

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Docker Compose is included in Docker Desktop for Windows and Mac, but you may need to install it separately on Linux. [Install Docker Compose](https://docs.docker.com/compose/install/)

### Setting Up the Dockerized Backend

Follow the steps below to set up and run the Django backend in a Dockerized environment:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/asifakram74/python-web-socket.git
    cd sync_hub
    ```

2. **Create and Configure Environment Variables**:

    Ensure that your `.env` file or environment variables are correctly set. The critical environment variables include:
    - `DATABASE_URL`: URL for the PostgreSQL database connection.
    - `REDIS_URL`: URL for the Redis connection.
    - `DJANGO_SETTINGS_MODULE`: Points to the settings file of your Django project.

    Example of environment variables:

    ```env
    DATABASE_URL=postgres://postgres:123456@db:5432/synchub_db
    REDIS_URL=redis://redis:6379/1
    DJANGO_SETTINGS_MODULE=sync_hub.settings
    ```

3. **Build and Run the Docker Containers**:

    Use Docker Compose to build the images and run the containers:

    ```bash
    docker-compose up --build
    ```

    This command will do the following:
    - Build the Docker images for the Django backend, PostgreSQL database, and Redis cache.
    - Create and start the Docker containers.
    - Run the Django application using Daphne to handle ASGI (WebSockets) requests.

4. **Apply Database Migrations**:

    Once the containers are up and running, apply the database migrations to set up the database schema:

    ```bash
    docker-compose run web python manage.py migrate
    ```

5. **Collect Static Files (Optional for Production)**:

    If you are deploying the project in a production environment, collect the static files:

    ```bash
    docker-compose run web python manage.py collectstatic --noinput
    ```

6. **Accessing the Application**:
    - **Backend**: The Django application will be available at `http://localhost:8000/` by default.
    - **Admin Panel**: Access the Django admin interface at `http://localhost:8000/admin/`.

### Managing Docker Containers

Here are some useful Docker Compose commands for managing the containers:

- **Stop the containers**:

    ```bash
    docker-compose down
    ```

- **Stop and remove containers, networks, images, and volumes**:

    ```bash
    docker-compose down --volumes --rmi all
    ```

- **View the logs**:

    ```bash
    docker-compose logs -f
    ```

- **Rebuild the images and restart the containers**:

    ```bash
    docker-compose up --build
    ```

### Notes

- Ensure that your `docker-compose.yml` and `Dockerfile` are correctly set up with the appropriate environment variables and dependencies.
- If you encounter any issues with Docker networking, ensure that the `db` and `redis` services are accessible from the `web` service by checking the network settings in Docker Compose.

### Troubleshooting

If you encounter any errors during the setup, consider the following steps:

- **Check the Docker Logs**: Use `docker-compose logs` to inspect the logs for any errors.
- **Database Connectivity**: Ensure that PostgreSQL and Redis are correctly set up and accessible from the Django application.
- **Environment Variables**: Double-check that all required environment variables are correctly set and accessible within the Docker containers.
