# Django RESTful API Project

This Django project provides a RESTful API for managing an inventory system with user authentication and item management capabilities.

## Setup and Running the Application

### Prerequisites
- Python 3
- pip
- Virtualenv (recommended)

### Installation
1. Clone the repository.
2. Navigate to the project directory.
3. (Optional) Setup a virtual environment and activate it.
4. Install dependencies: `pip install -r requirements.txt`.

### Running the Server
Execute `python3 manage.py runserver` to start the development server.

### Database Setup
The project uses SQLite. Use the SQLite extension in Visual Studio Code to manage the database.

### Applying Migrations
Create and apply migrations to reflect model changes in the database:`python3 manage.py makemigrations`, `python3 manage.py migrate`

## API Usage

### Endpoints
- **Register**: `POST /api/v1/auth/register/`
- **Login**: `POST /api/v1/auth/login/` (returns an auth token)
- **Items**: `GET /api/v1/items` (requires auth token)
- **Inventory**: `GET /api/v1/inventory` (supports filtering with query parameters)

### Authorization
Protected endpoints require a valid token in the Authorization header:
 Authorization: Bearer <YOUR_ACCESS_TOKEN>
 Remember to replace <YOUR_ACCESS_TOKEN> with the actual token received upon authentication.

## Testing
Run tests using the command: `python3 manage.py test items`.



