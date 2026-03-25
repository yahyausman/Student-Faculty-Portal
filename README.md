# Student & Faculty Portal

A web-based portal for a university environment that allows students and faculty members to register, log in, and manage their academic information. All data is stored in a MySQL database and served through a Python Flask backend.

---

## Features

### Student Dashboard
- Student registration with personal and academic details
- Secure login system
- View and edit personal profile
- View enrolled courses
- View academic records and grades

### Faculty System
- Faculty registration with professional details
- Secure login system
- View and edit personal profile
- View assigned courses and teaching load
- Access student records for enrolled students

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Database | MySQL |

---

## Project Structure

```
student-faculty-portal/
├── app.py                  # Flask backend
└── templates/
    └── dashboard.html      # Main frontend interface
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/student-faculty-portal.git
cd student-faculty-portal
```

### 2. Install dependencies
```bash
pip install flask mysql-connector-python
```

### 3. Set up the database
Open MySQL Workbench and run the following SQL:

```sql
CREATE DATABASE academia_db;

USE academia_db;

CREATE TABLE students (
    student_id    VARCHAR(20) PRIMARY KEY,
    first_name    VARCHAR(100) NOT NULL,
    last_name     VARCHAR(100) NOT NULL,
    email         VARCHAR(255) UNIQUE NOT NULL,
    password      VARCHAR(255) NOT NULL,
    department    VARCHAR(100),
    year_of_study VARCHAR(20),
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE TABLE faculty (
    employee_id    VARCHAR(20) PRIMARY KEY,
    first_name     VARCHAR(100) NOT NULL,
    last_name      VARCHAR(100) NOT NULL,
    email          VARCHAR(255) UNIQUE NOT NULL,
    password       VARCHAR(255) NOT NULL,
    department     VARCHAR(100) NOT NULL,
    title          VARCHAR(60),
    specialization VARCHAR(255),
    created_at     TIMESTAMP DEFAULT NOW()
);
```

### 4. Configure the database connection
Open `app.py` and update the password:
```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",  # change this
        database="academia_db"
    )
```

### 5. Run the application
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## Database Schema

### Students Table
| Field | Type | Description |
|-------|------|-------------|
| student_id | VARCHAR(20) | Primary key |
| first_name | VARCHAR(100) | First name |
| last_name | VARCHAR(100) | Last name |
| email | VARCHAR(255) | Unique email |
| password | VARCHAR(255) | Account password |
| department | VARCHAR(100) | Department name |
| year_of_study | VARCHAR(20) | Academic year |
| created_at | TIMESTAMP | Registration date |

### Faculty Table
| Field | Type | Description |
|-------|------|-------------|
| employee_id | VARCHAR(20) | Primary key |
| first_name | VARCHAR(100) | First name |
| last_name | VARCHAR(100) | Last name |
| email | VARCHAR(255) | Unique email |
| password | VARCHAR(255) | Account password |
| department | VARCHAR(100) | Department |
| title | VARCHAR(60) | Academic title |
| specialization | VARCHAR(255) | Research area |
| created_at | TIMESTAMP | Registration date |

---

## Usage

1. Open the portal at `http://127.0.0.1:5000`
2. Select your role: Student or Faculty
3. Register a new account or log in with existing credentials
4. Access your dashboard to view and manage your information

---

## Author

Developed as part of a university database management assignment.
