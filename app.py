from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# ── Connect to MySQL ──
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yahya123",  
        database="academia_db"
    )

# ── Home page ──
@app.route('/')
def home():
    return render_template('dashboard.html')

# ── Student Registration ──
@app.route('/register/student', methods=['POST'])
def register_student():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO students (student_id, first_name, last_name, email, password, department, year_of_study) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (
                request.form['studentId'],
                request.form['firstName'],
                request.form['lastName'],
                request.form['email'],
                request.form['password'],
                request.form['dept'],
                request.form['year']
            )
        )
        db.commit()
        return jsonify({'success': True})
    except mysql.connector.IntegrityError:
        return jsonify({'success': False, 'error': 'Student ID or Email already exists'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ── Student Login ──
@app.route('/login/student', methods=['POST'])
def login_student():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s AND password=%s",
            (request.form['studentId'], request.form['password'])
        )
        student = cursor.fetchone()
        if student:
            session['user'] = dict(student)
            session['role'] = 'student'
            return jsonify({'success': True, 'user': {
                'firstName': student['first_name'],
                'lastName': student['last_name'],
                'email': student['email'],
                'studentId': student['student_id'],
                'dept': student['department'],
                'year': student['year_of_study'],
                'created': str(student['created_at'])
            }})
        return jsonify({'success': False, 'error': 'Invalid Student ID or password'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ── Faculty Registration ──
@app.route('/register/faculty', methods=['POST'])
def register_faculty():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO faculty (employee_id, first_name, last_name, email, password, department, title, specialization) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                request.form['employeeId'],
                request.form['firstName'],
                request.form['lastName'],
                request.form['email'],
                request.form['password'],
                request.form['dept'],
                request.form['title'],
                request.form['spec']
            )
        )
        db.commit()
        return jsonify({'success': True})
    except mysql.connector.IntegrityError:
        return jsonify({'success': False, 'error': 'Employee ID or Email already exists'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ── Faculty Login ──
@app.route('/login/faculty', methods=['POST'])
def login_faculty():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM faculty WHERE employee_id=%s AND password=%s",
            (request.form['employeeId'], request.form['password'])
        )
        faculty = cursor.fetchone()
        if faculty:
            session['user'] = dict(faculty)
            session['role'] = 'faculty'
            return jsonify({'success': True, 'user': {
                'firstName': faculty['first_name'],
                'lastName': faculty['last_name'],
                'email': faculty['email'],
                'employeeId': faculty['employee_id'],
                'dept': faculty['department'],
                'title': faculty['title'],
                'spec': faculty['specialization'],
                'created': str(faculty['created_at'])
            }})
        return jsonify({'success': False, 'error': 'Invalid Employee ID or password'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ── Dashboard ──
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html')

# ── Logout ──
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)