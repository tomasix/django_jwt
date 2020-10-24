# Django JWT Auth

## Installation
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

## Usage

Users could be managed via HTML http://127.0.0.1:8000/admin/

API 
api/v1/token-auth/
``` curl -X POST -H "Content-Type: application/json" -d '{"username":"youruser","password":"yourpassword"}' http://localhost:8000/api/v1/token-auth/ ```

api/v1/token-refresh/
``` curl -X POST -H "Content-Type: application/json" -d '{"token":"yourtoken"}' http://localhost:8000/api/v1/token-refresh/ ```

api/v1/token-verify/ 
``` curl -X POST -H "Content-Type: application/json" -d '{"token":"yourtoken"}' http://localhost:8000/api/v1/token-verify/ ```

## Useful links

https://docs.djangoproject.com/en/3.1/
https://styria-digital.github.io/django-rest-framework-jwt/
