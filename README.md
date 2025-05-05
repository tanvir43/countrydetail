
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

### 1. Clone the Repository

```bash
git clone https://github.com/tanvir43/countrydetail.git
cd countrydetail
```

### 2. Create a Virtual Environment

```bash
python3 -m venv my_env
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn’t exist yet, here are the essentials:

```bash
pip install django djangorestframework djangorestframework-simplejwt requests drf-yasg
```

---

## Configuration

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Create SuperUser

```bash
python manage.py createsuperuser
```

## Fetch and Store data from [REST Countries API](https://restcountries.com/v3.1/all)

```bash
python manage.py fetch_countries
```

## API doc
```bash
python manage.py runserver
```
[Swagger](http://http://localhost:8000/swagger/)
[redoc](http://localhost:8000/redoc/)

