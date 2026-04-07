# Adam API backend

Backend for Eva app. Built with Django REST Framework. Provides REST API for file storage with automatic file validation at model level. Uses SQLite as default database. Files are stored in `media/saves/` directory.

### API Endpoints

- General
  - `GET`       `/api/` - API root with links to all endpoints.
  - `GET`       `/api/redoc/` - ReDoc API documentation.
  - `GET`       `/admin/` - Django admin panel.

- Saves
  - `GET`       `/api/saves/` - Get list of all saves.
  - `POST`      `/api/saves/` - Create new save (file required).
  - `GET`       `/api/saves/{id}/` - Get save details.
  - `PUT`       `/api/saves/{id}/` - Update save.
  - `PATCH`     `/api/saves/{id}/` - Partially update save.
  - `DELETE`    `/api/saves/{id}/` - Delete save (removes file from disk).
  - `GET`       `/api/saves/{id}/download/` - Download save file.

## Usage
You can open root url in browser to see the GUI interface for app. Or use this `curl` snippets to create files directly:

```sh
# Create new save with file
curl -X POST http://localhost:8000/api/saves/ \
-F "save_file=@.json"

# Response
{"id":1,"created_at":"2024-01-15T10:30:00Z","updated_at":"2024-01-15T10:30:00Z","save_file":"/media/saves/file.zip"}

# Download save file
curl -X GET http://localhost:8000/api/saves/1/download/ \
--output downloaded_file.zip

# Delete save
curl -X DELETE http://localhost:8000/api/saves/1/

# Response
{"status":"deleted","save_id":1}
```

## Setup
Install dependencies and apply migrations:

```sh
# Install requirements
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create admin
python3 manage.py createsuperuser
```

Run development server:
```sh
python3 manage.py runserver
```

App will be available at localhost:8000.

## Models
Stores uploaded files with timestamps.

id - Auto-increment primary key
save_file - File field (required, rejects empty files)
created_at - Creation timestamp
updated_at - Last update timestamp
