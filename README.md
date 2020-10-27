# Django JWT Auth
Please keep in mind that this is only demo for developement / education environment, don't use it as it is in production.


## Installation
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
gunicorn django_login.wsgi
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




There is Prometheus monitoring enabled, for detailed HOWTO please see: https://www.sipios.com/blog-tech/monitoring


## Useful links

 - https://docs.djangoproject.com/en/3.1/
 - https://styria-digital.github.io/django-rest-framework-jwt/
 - https://docs.gunicorn.org/en/latest/index.html
 - https://prometheus.io/
