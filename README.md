# Django Product API Project

This project is a Django-based backend system designed to manage and expose product-related data via REST APIs.

---

## 🚀 Setup Instructions

### Clone the repository:
```bash
git clone https://github.com/yourusername/project.git
cd project
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧩 Project Structure

```
project/
├── manage.py
├── db.sqlite3
├── requirements.txt
└── products/
    ├── admin.py
    ├── models.py
    ├── serializers.py
    ├── tasks.py
    ├── tests.py
    └── views.py
```

---

## 🌐 API Endpoints

| Endpoint              | Method | Description               |
|-----------------------|--------|---------------------------|
| `/api/products/`      | GET    | List all products         |
| `/api/products/<id>/` | GET    | Retrieve a single product |
| `/api/products/`      | POST   | Create a new product      |

> More endpoints may exist depending on `views.py`.

---

## 🛠️ Database Schema (Simplified)

### Product Model

- `id`: Integer (Primary Key)  
- `name`: CharField  
- `description`: TextField  
- `price`: DecimalField  
- `created_at`: DateTimeField  

---

## 🏛 Architectural Overview

- **Framework**: Django 4.x  
- **API**: Django REST Framework  
- **Database**: SQLite (can be replaced with PostgreSQL/MySQL)  
- **Async Tasks**: Celery (used in `tasks.py`)  
- **Containerization**: Docker + Docker Compose  

---

## 📋 Code Review Checklist for Junior Developers

### ✅ API Endpoint Design

- Are URLs RESTful and consistent?  
- Are serializers used for input/output validation?  
- Is API documentation (e.g., docstrings or Swagger) present?  

### ✅ Database Optimization

- Are `select_related` and `prefetch_related` used where appropriate?  
- Are there any N+1 query issues?  
- Are indexes defined on frequently filtered fields?  

### ✅ Django Best Practices

- Are class-based views used where reusable patterns exist?  
- Are third-party packages like DRF used effectively?  
- Is the `admin.py` customized for better usability?  

---

## 👶 Onboarding Plan for Junior Developer

**Day 1–2**

- Set up the project locally using the README  
- Explore folder structure and key modules (models, serializers, views)  

**Day 3–5**

- Walk through one API flow from request to response  
- Run the test suite and review sample test cases  

**Week 2**

- Implement a simple feature or bug fix with a code review  
- Write one or two unit tests  
- Join sprint planning and standups to understand the team workflow  

**Ongoing**

- Participate in peer code reviews using the checklist above  
- Regularly sync with a mentor or lead developer  

---

## 📦 Deployment Notes

- Use the provided `Dockerfile` and `docker-compose.yml` for containerized development.  
- Ensure production environment variables (e.g., secrets, DB settings) are securely managed.
