import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

students_db = mysql.connector.connect(user="sql6513769",
                                      password="2aWYts84wC",
                                      host="sql6.freesqldatabase.com",
                                      database="sql6513769")
cursor = students_db.cursor()


def check_email_exists(email):
    query = f"SELECT * FROM users WHERE email ='{email}'"
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False


def check_valid_password(email, password):
    query = f"SELECT * FROM users WHERE email ='{email}'"
    cursor.execute(query)
    result = cursor.fetchall()

    print(result)

    if len(result) > 0:
        print(check_password_hash(result[0][-1], password))
        if check_password_hash(result[0][-1], password):
            return True

    return False


def get_user_data(email, password):
    query = f"SELECT * FROM users WHERE email ='{email}'"
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) > 0:
        if check_password_hash(result[0][-1], password):
            return result[0]

    return ()


def get_students(student_class=None, name=None):

    if name:
        query = f"SELECT * FROM students WHERE name='{name}';"
    elif student_class:
        query = f"SELECT * FROM students WHERE class='{student_class}' ORDER BY class"
    else:
        query = "SELECT * FROM students ORDER BY class;"

    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) > 0:
        return result
    else:
        return []
