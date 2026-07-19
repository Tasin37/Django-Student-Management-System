# Django Student Management System

A comprehensive REST API-based Student Management System built with Django and Django REST Framework. This system manages departments, teachers, students, academic results, and department hierarchies within an educational institution.

##  Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Models](#database-models)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Validation Rules](#validation-rules)
- [Admin Interface](#admin-interface)
- [Development](#development)

---

##  Overview

This Django application provides a complete backend solution for managing educational institutions. It handles:

- **Departments**: Creation and management of academic departments
- **Teachers**: Faculty information and department assignments
- **Students**: Student enrollment and academic records
- **Results**: Academic performance tracking and grading
- **Department Heads**: Administrative hierarchy management

The system exposes RESTful APIs with pagination, filtering, searching, and ordering capabilities for efficient data management.

---

##  Features

-  **Full CRUD Operations**: Create, Read, Update, and Delete for all entities
-  **Advanced Filtering**: Filter data by specific criteria (e.g., building, departments)
-  **Search Functionality**: Full-text search across departments, teachers, and students
-  **Sorting/Ordering**: Order results by various fields (e.g., salary)
-  **Pagination**: API responses are paginated (5 items per page by default)
-  **Data Validation**: Custom validators for business logic (salary validation, marks validation)
-  **Relationships**: Many-to-many and one-to-one relationships properly managed
-  **Nested Serialization**: Related data returned with parent objects
-  **Timestamps**: Automatic creation and update timestamps on all models
-  **Django Admin Interface**: Full admin panel for management
-  **Inline Editing**: Edit related students directly within department admin page

---

##  Tech Stack

| Technology | Version |
|------------|---------|
| Django | 6.0.7 |
| Django REST Framework | 3.17.1 |
| django-filters | 26.1 |
| asgiref | 3.12.1 |
| Python | 3.x |
| SQLite | (Database) |

---

##  Project Structure

```
django-Student Management System/
│
├── core/                          # Main project configuration
│   ├── __init__.py
│   ├── settings.py               # Django settings and configurations
│   ├── urls.py                   # URL routing configuration
│   ├── asgi.py                   # ASGI application entry point
│   └── wsgi.py                   # WSGI application entry point
│
├── faculty/                       # Main application
│   ├── migrations/               # Database migration files
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_result_marks_alter_result_unique_together.py
│   ├── __init__.py
│   ├── admin.py                  # Django admin configurations
│   ├── apps.py                   # Application configuration
│   ├── models.py                 # Database models
│   ├── serializers.py            # DRF serializers
│   ├── validators.py             # Custom validators
│   ├── views.py                  # API views and viewsets
│   └── tests.py                  # Unit tests
│
├── myenv/                        # Virtual environment (Python packages)
│   └── Lib/site-packages/        # Installed dependencies
│
├── manage.py                     # Django management script
├── db.sqlite3                    # SQLite database file
└── README.md                     # This file
```

---

##  Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step-by-Step Installation

1. **Clone or extract the project**
   ```bash
   cd "d:\django- Student Management System"
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv myenv
   myenv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or manually install:
   ```bash
   pip install Django==6.0.7
   pip install djangorestframework==3.17.1
   pip install django-filter==26.1
   pip install asgiref==3.12.1
   ```

4. **Run migrations** (database setup)
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create admin credentials.

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The server will start at `http://127.0.0.1:8000/`

---

##  Configuration

### Key Settings (core/settings.py)

- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Configure allowed hosts before deployment
- **SECRET_KEY**: Change in production
- **DATABASE**: Uses SQLite by default (change for production environments)
- **REST_FRAMEWORK Settings**:
  - Pagination: 5 items per page
  - Filters: DjangoFilterBackend, SearchFilter, OrderingFilter
  - CORS: Not configured by default (add if needed)

### Database Configuration

Currently uses SQLite (`db.sqlite3`). To use PostgreSQL or MySQL:

1. Install database driver: `pip install psycopg2` (PostgreSQL)
2. Update `DATABASES` in `core/settings.py`

---

##  Database Models

### 1. **Department**
Represents academic departments within the institution.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (auto-generated) |
| name | CharField(50) | Department name (required) |
| building | CharField(100) | Building location |
| mission | TextField | Department mission statement |
| established_on | DateField | Establishment date |
| created_at | DateTime | Auto-generated creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

**Relationships:**
- Has many Teachers (many-to-many)
- Has many Students (one-to-many)
- Has one DepartmentHead (one-to-one)

---

### 2. **Teacher**
Represents faculty members and instructors.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (auto-generated) |
| name | CharField(50) | Teacher's full name (required) |
| email | EmailField | Unique email address |
| salary | DecimalField | Monthly salary (10 digits, 2 decimal places) |
| department | ManyToManyField | Associated departments |
| created_at | DateTime | Auto-generated creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

**Validation:**
- Email must be unique
- Salary must be greater than 0

**Relationships:**
- Associated with multiple Departments (many-to-many)
- Can be a DepartmentHead (one-to-one)

---

### 3. **Student**
Represents enrolled students in the institution.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (auto-generated) |
| name | CharField(50) | Student's full name (required) |
| student_id | CharField(20) | Unique student identifier |
| email | EmailField | Unique email address |
| department | ForeignKey | Associated department |
| created_at | DateTime | Auto-generated creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

**Validation:**
- Student ID must be unique
- Email must be unique
- Department is required

**Relationships:**
- Belongs to one Department (foreign key)
- Has many Results (one-to-many)

---

### 4. **Result**
Stores academic performance data for students.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (auto-generated) |
| student | ForeignKey | Associated student (required) |
| subject_code | CharField(10) | Course/subject code |
| marks | FloatField | Student's marks/score |
| created_at | DateTime | Auto-generated creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

**Validation:**
- Marks must be between 0 and 100 (inclusive)
- Unique constraint: A student can only have one result per subject

**Relationships:**
- Belongs to one Student (foreign key)

---

### 5. **DepartmentHead**
Manages the administrative hierarchy of departments.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (auto-generated) |
| department | OneToOneField | Associated department (unique) |
| teacher | OneToOneField | Head teacher (unique) |
| created_at | DateTime | Auto-generated creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

**Relationships:**
- One-to-one with Department
- One-to-one with Teacher

---

##  API Endpoints

All endpoints use JSON for request/response bodies. The API is paginated with 5 items per page by default.

### Base URL
```
http://127.0.0.1:8000
```

### Department Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/department/` | List all departments (with filtering, search, ordering) |
| POST | `/api/department/` | Create a new department |
| GET | `/api/department/<id>/` | Retrieve a specific department |
| PUT | `/api/department/<id>/` | Update a department |
| DELETE | `/api/department/<id>/` | Delete a department |

**Query Parameters:**
- `building`: Filter by building name
- `search`: Search by department name
- `ordering`: Order by name (e.g., `?ordering=name` or `?ordering=-name`)
- `page`: Pagination (e.g., `?page=1`)

---

### Student Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/student/` | List all students |
| POST | `/api/student/` | Create a new student |
| GET | `/api/student/<id>/` | Retrieve a specific student |
| PUT | `/api/student/<id>/` | Update a student (full update) |
| PATCH | `/api/student/<id>/` | Partial update a student |
| DELETE | `/api/student/<id>/` | Delete a student |

---

### Teacher Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/teacher/` | List all teachers (with ordering by salary) |
| POST | `/api/teacher/` | Create a new teacher |
| GET | `/api/teacher/<id>/` | Retrieve a specific teacher |
| PUT | `/api/teacher/<id>/` | Update a teacher (full update) |
| PATCH | `/api/teacher/<id>/` | Partial update a teacher |
| DELETE | `/api/teacher/<id>/` | Delete a teacher |

**Query Parameters:**
- `ordering`: Order by salary (e.g., `?ordering=salary` or `?ordering=-salary` for descending)

---

### Result Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/result/` | List all results |
| POST | `/api/result/` | Create a new result/grade |
| GET | `/api/result/<id>/` | Retrieve a specific result |
| PUT | `/api/result/<id>/` | Update a result (full update) |
| PATCH | `/api/result/<id>/` | Partial update a result |
| DELETE | `/api/result/<id>/` | Delete a result |

---

### Department Head Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/department-head/` | List all department heads |
| POST | `/api/department-head/` | Create a new department head assignment |
| GET | `/api/department-head/<id>/` | Retrieve a specific department head |
| PUT | `/api/department-head/<id>/` | Update a department head assignment |
| PATCH | `/api/department-head/<id>/` | Partial update a department head |
| DELETE | `/api/department-head/<id>/` | Delete a department head assignment |

---

##  Usage Examples

### 1. Create a Department

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/department/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Computer Science",
    "building": "CS Building",
    "mission": "To produce skilled computer scientists",
    "established_on": "2010-01-15"
  }'
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Computer Science",
  "building": "CS Building",
  "mission": "To produce skilled computer scientists",
  "established_on": "2010-01-15",
  "students": [],
  "teachers": [],
  "created_at": "2024-07-19T10:30:00Z",
  "updated_at": "2024-07-19T10:30:00Z"
}
```

### 2. Create a Teacher

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/teacher/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dr. John Smith",
    "email": "john.smith@university.edu",
    "salary": "65000.00",
    "department": [1]
  }'
```

### 3. Create a Student

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/student/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "student_id": "CS001",
    "email": "alice.johnson@student.edu",
    "department": 1
  }'
```

### 4. Add Student Results

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/result/ \
  -H "Content-Type: application/json" \
  -d '{
    "student": 1,
    "subject_code": "CS101",
    "marks": 85.5
  }'
```

### 5. Get Department with Related Data

**Request:**
```bash
curl http://127.0.0.1:8000/api/department/1/
```

**Response:** Returns department with all related students and teachers

### 6. Search Departments

**Request:**
```bash
curl "http://127.0.0.1:8000/api/department/?search=Computer"
```

### 7. Order Teachers by Salary

**Request:**
```bash
curl "http://127.0.0.1:8000/api/teacher/?ordering=-salary"
```

This returns teachers sorted by salary in descending order.

---

##  Validation Rules

### Department Validation
- **name**: Required, case-insensitive uniqueness (no duplicate department names)
- **building**: Required
- **mission**: Required
- **established_on**: Required, must be a valid date

### Teacher Validation
- **name**: Required, max 50 characters
- **email**: Required, must be unique and valid email format
- **salary**: Required, must be greater than 0
- **department**: At least one department should be assigned

### Student Validation
- **name**: Required, max 50 characters
- **student_id**: Required, unique identifier
- **email**: Required, must be unique and valid email format
- **department**: Required, must be a valid department

### Result Validation
- **student**: Required, must be a valid student
- **subject_code**: Required, max 10 characters
- **marks**: Required, must be between 0 and 100 (inclusive)
- **Unique Constraint**: A student can only have one result per subject_code

### DepartmentHead Validation
- **department**: Required, must be unique (only one head per department)
- **teacher**: Required, must be unique (each teacher can only head one department)

---

##  Admin Interface

The Django admin interface is available at `/admin/` and provides a user-friendly way to manage data.

### Access Admin Panel
1. Navigate to: `http://127.0.0.1:8000/admin/`
2. Log in with superuser credentials
3. Manage all entities through the admin interface

### Admin Features

**Department Admin**
- List view with columns: ID, Name, Building, Mission
- Search by department name
- Sorted alphabetically
- Inline editing of students within department

**Teacher Admin**
- List view with columns: ID, Name, Email, Salary
- Search by name and email
- Sorted alphabetically
- Horizontal filter for department assignments

**Student Admin**
- List view with columns: Student ID, Name, Department
- Search by name and student ID
- Filtered by department
- Sorted alphabetically

---

##  Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

After modifying models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Shell

Access Python interactive shell with Django models:
```bash
python manage.py shell
```

Example:
```python
from faculty.models import Department
dept = Department.objects.create(
    name="Engineering",
    building="ENG-1",
    mission="Excellence in engineering",
    established_on="2015-01-01"
)
```

### Linting and Code Quality

It's recommended to use:
- `flake8` for style guide enforcement
- `black` for code formatting
- `pylint` for code analysis

### Deployment Considerations

Before deploying to production:

1. Set `DEBUG = False` in settings
2. Update `ALLOWED_HOSTS` with your domain
3. Use a strong `SECRET_KEY`
4. Switch to production database (PostgreSQL recommended)
5. Use environment variables for sensitive data
6. Set up proper logging
7. Configure CORS if serving frontend separately
8. Use gunicorn or similar WSGI server
9. Set up HTTPS/SSL certificate
10. Configure static and media file serving

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0.7 | Web framework |
| djangorestframework | 3.17.1 | REST API framework |
| django-filter | 26.1 | Advanced filtering for APIs |
| asgiref | 3.12.1 | ASGI utilities |

---

##  License

This project is part of an educational system. Use and modify as needed.

---

##  Support

For issues or questions:
1. Check the Django documentation: https://docs.djangoproject.com/
2. Check DRF documentation: https://www.django-rest-framework.org/
3. Review the code comments and docstrings

---

##  Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Guide](https://www.django-rest-framework.org/)
- [django-filter Documentation](https://django-filter.readthedocs.io/)
- [RESTful API Best Practices](https://restfulapi.net/)

---

**Last Updated**: July 19, 2024  
**Version**: 1.0.0
"# Django-Student-Management-System" 
