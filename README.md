Pharma Filter System Backend
This project is the backend for a pharmaceutical filter tracking and management system. It is built with Django and Django REST Framework, providing a robust API for managing filters, cleaning records, user roles, and generating reports.
Features
User Management: Handles different user roles (admin, supervisor, operator) and provides secure authentication.
Filter Tracking: Manages information about different types of filters, their locations (AHUs and Plants), and their status.
Cleaning Records: Records detailed information about the cleaning process for each filter, including dates, times, and status.
Audit Logging: Logs all changes to key models to provide a full audit trail.
API Endpoints: Exposes a RESTful API for all system resources.
Dockerized Environment: Provides a containerized setup for easy and consistent deployment in any environment.
Technologies Used
Django: A high-level Python web framework.
Django REST Framework: A powerful toolkit for building Web APIs.
SQLite3: A lightweight, file-based database for development.
Gunicorn: A Python WSGI HTTP Server for UNIX.
Docker & Docker Compose: Containerization tools for managing the application environment.
Prerequisites
Docker: Ensure Docker is installed and running on your system.
Docker Compose: Ensure Docker Compose is installed.
Getting Started
Follow these steps to get the backend up and running in a Docker container.
Clone the repository:
git clone <your-repo-url>
cd pharma-filter-system-backend


Create a .env file:
Create a file named .env in the root directory. This is not strictly necessary for this setup, but it's good practice for future environment variables. For now, you can leave it empty.
Build the Docker image:
This command reads the Dockerfile and builds a Docker image for your application.
docker-compose build


Run database migrations and create a superuser:
These commands set up the database schema and create an initial admin user to access the Django admin panel. You will be prompted to enter a username, email, and password for the admin user.
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser


Start the services:
This command starts the web server in the container. The -d flag runs it in detached mode (in the background).
docker-compose up -d


The application should now be running and accessible at http://localhost:8000.
API Endpoints
The API is available at http://localhost:8000/api/. Here is a summary of the main endpoints:
/api/users/: Manage user accounts.
/api/plants/: Manage plants.
/api/ahus/: Manage AHUs (Air Handling Units).
/api/filter-types/: Manage filter types.
/api/filters/: Manage individual filters.
/api/cleaning-records/: Manage filter cleaning records.
/api/audit-logs/: View audit log entries.
/api/token/: Obtain JWT access and refresh tokens.
Django Admin Panel
You can access the Django admin panel at http://localhost:8000/admin/ with the superuser credentials you created during the setup.
License
This project is licensed under the MIT License. See the LICENSE file for details.
