
# Django Country Info App

This application fetches data from the [REST Countries API](https://restcountries.com/v3.1/all), stores it in a Django database, and provides a secure API and web interface to explore country information.

---

## Features

- RESTful API to list, retrieve, search, filter countries.
- Bootstrap-styled searchable UI and detail views.
- Authentication for both API and web access.
- Country detail view shows languages and regional neighbors.

---

## Installation

### 1. Create a Virtual Environment

```bash
python3 -m venv my_env
source venv/bin/activate  # On Windows: venv\Scripts\activate

``` 


### 2. Create a project folder

```bash
mkdir project-folder

```

### 3. Go to your project folder

```bash
cd project-folder

```

### 4. Intialize Git

```bash
git init
```

### 5. Clone the Repository

```bash
git clone https://github.com/tanvir43/countrydetail.git
cd countrydetail
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn’t exist yet, here are the essentials:

```bash
pip install django djangorestframework djangorestframework-simplejwt requests drf-yasg djangorestframework-simplejwt

```

---

## Configuration

### 1. Apply Migrations

```bash
python manage.py migrate

```

### 2. Make sure you run collectstatic command

```bash
python manage.py collectstatic

```

### 3. Create SuperUser

```bash
python manage.py createsuperuser

```

### 4. Run local server

```bash
python manage.py runserver

```

### 5. Login with django admin panel
Go to http://localhost:8000/admin (8000 is default port, use your provided port if available)


### 6. If data is not available, fetch and store data from [REST Countries API](https://restcountries.com/v3.1/all)

```bash
python manage.py fetch_countries

```

### 7. Run local server again

```bash
python manage.py runserver

```

### 8. For web view
Go to http://localhost:8000 (8000 is a default port, use your provided port if available)

### 9. For API doc(Swagger)
Go to http://localhost:8000/swagger/ (8000 is a default port, use your provided port if available)


[Swagger](http://localhost:8000/swagger/)


## Get token

### Go to /api/token/ and get a access token (you can do this from Swagger too, go bottom of the swagger api doc).

POST your username and password

```bash
{
  "username": "your_user",
  "password": "your_pass"
}
```

### Click authorize button and pass the access token

```bash
Bearer <access_token>

```

