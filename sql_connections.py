import mysql.connector

students_db = mysql.connector.connect(user="sql6520785",
                                      password="gVBlZdazDt",
                                      host="sql6.freesqldatabase.com",
                                      database="sql6520785")
cursor = students_db.cursor()


def get_students(student_class=None, name=None):
    if name:
        query = f"SELECT * FROM students WHERE name='{name}';"
    elif student_class:
        query = f"SELECT * FROM students WHERE class='{student_class}' ORDER BY class"
    else:
        query = "SELECT * FROM students ORDER BY class;"

    cursor.execute(query)
    result = cursor.fetchall()

    print(result)
    if len(result) > 0:
        return result
    else:
        return []


def register_student(name,
                     grade,
                     father_name,
                     mother_name,
                     father_phone,
                     mother_phone,
                     roll,
                     address):
    query = f"INSERT INTO students (`name`, `class`, `father_name`, `mother_name`, `address`, `father_no`, `mother_no`, `roll_no`)  VALUES ('{name}', '{grade}', '{father_name}', '{mother_name}', '{address}', '{father_phone}', '{mother_phone}', '{roll}')"
    cursor.execute(query)
    students_db.commit()


def validate_new_student(grade, roll):
    query = f"SELECT * FROM students WHERE class='{grade}' AND roll_no='{roll}'"
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) > 0:
        return False
    else:
        return True


def get_student_details(student_id):
    query = f"SELECT * FROM students WHERE id={student_id}"
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) > 0:
        return result
    else:
        return []


def delete_student_sql(student_id):
    query = f"DELETE FROM students WHERE id={student_id}"
    cursor.execute(query)
    students_db.commit()
