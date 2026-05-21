# Adam API backend

Backend for Eva app. Built with Django REST Framework. Provides REST API for file storage with automatic file validation at model level. Uses SQLite as default database. Files are stored in `media/saves/` directory.

> [!NOTE]  
> Cliend app is located in [separate repository](https://github.com/Catalyst-42/Adam)

## Images
| ![API Root](<img/Adam - Root.png>) | ![RPI Save list](<img/Adam - Save list.png>) |
|-|-|

## API Endpoints

- Actual schema may be seen in `/api/redoc` route

- General
  - `GET`       `/api/` - API root with links to all endpoints.
  - `GET`       `/api/redoc/` - ReDoc API documentation.
  - `GET`       `/admin/` - Django admin panel.

- Saves
  - `GET`       `/api/saves/` - Get list of all saves.
  - `POST`      `/api/saves/` - Create new save.
  - `GET`       `/api/saves/{id}/` - Get save details.
  - `PUT`       `/api/saves/{id}/` - Update save.
  - `PATCH`     `/api/saves/{id}/` - Partially update save.
  - `DELETE`    `/api/saves/{id}/` - Delete save.

## Setup
Install dependencies and apply common django actions:

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
python3 manage.py runserver 0.0.0.0:8000
```

App will be available at `localhost:8000`.

## Models
App stores uploaded files with timestamps.

id - Auto-increment primary key  
save_file - File field  
created_at - Creation timestamp  
updated_at - Last update timestamp  
