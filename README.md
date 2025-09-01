Pharma Filter System Backend

This project is the backend for a pharmaceutical filter tracking and management system.
It is built with Django and Django REST Framework, providing a robust API for managing filters, cleaning records, user roles, and generating reports.

🚀 Features

User Management: Handles different user roles (admin, supervisor, operator) with secure authentication.

Filter Tracking: Manages filters, their locations (AHUs and Plants), and their statuses.

Cleaning Records: Stores detailed cleaning information (dates, times, and status).

Audit Logging: Tracks all key model changes to ensure a complete audit trail.

API Endpoints: Provides a RESTful API for all system resources.

Dockerized Environment: Containerized setup for consistent deployment.

🛠 Technologies Used

Django – High-level Python web framework

Django REST Framework (DRF) – Toolkit for building Web APIs

SQLite3 – Lightweight, file-based database (for development)

Gunicorn – WSGI HTTP Server for UNIX

Docker & Docker Compose – Containerization tools

📋 Prerequisites

Docker
 installed and running

Docker Compose
 installed

⚡ Getting Started

Follow these steps to run the backend in a Docker container:

1. Clone the Repository
git clone <your-repo-url>
cd pharma-filter-system-backend

2. Create a .env File

Create a file named .env in the root directory.
(It can be empty for now, but useful for future environment variables.)

3. Build the Docker Image
docker-compose build

4. Run Database Migrations and Create Superuser
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser


➡️ You’ll be prompted to enter a username, email, and password.

5. Start the Services
docker-compose up -d


Now, the application should be running at:
👉 http://localhost:8000

📡 API Endpoints

Base URL: http://localhost:8000/api/

Endpoint	Description
/api/users/	Manage user accounts
/api/plants/	Manage plants
/api/ahus/	Manage AHUs (Air Handling Units)
/api/filter-types/	Manage filter types
/api/filters/	Manage individual filters
/api/cleaning-records/	Manage filter cleaning records
/api/audit-logs/	View audit log entries
/api/token/	Obtain JWT access & refresh tokens
🛠 Django Admin Panel

Access the admin panel at:
👉 http://localhost:8000/admin/

Use the superuser credentials you created during setup.

📄 License

This project is licensed under the MIT License.
See the LICENSE
 file for details.