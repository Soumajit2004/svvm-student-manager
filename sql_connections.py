import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

students_db = mysql.connector.connect(user="server",
                                      password="gcp-server-mysql",
                                      host="34.131.201.218",
                                      database="students")
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
