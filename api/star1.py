from bottle import route, get, post, delete, put, run, request
import pymysql
import json

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="students",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@route("/")
def root():
    return "work"


@get('/student/<id:int>')
def get_student(id):
    try:
        with connection.cursor() as cursor:
            sql = "select * from stu where id = {}".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result)
    except:
        raise Exception


@post('/students')
def add_student():
    try:
        first_name = request.json.get("full_name")
        cohort = request.json.get("cohort")
        with connection.cursor() as cursor:
            sql = "INSERT INTO stu (full_name,cohort) VALUES('{}', '{}')".format(
                first_name, cohort)
            cursor.execute(sql)
            connection.commit()
            return 'Student Added!'
    except:
        raise Exception


@put('/students')
def update_student():
    try:
        i_d = request.json.get("id")
        name = request.json.get("full_name")
        cohort = request.json.get("cohort")
        with connection.cursor() as cursor:
            sql = f"UPDATE stu SET full_name = '{name}', cohort = '{cohort}' WHERE id = '{i_d}'"
            cursor.execute(sql)
            connection.commit()
            return 'Student was updated!'
    except:
        raise Exception


@delete('/students')
def delete_student():
    try:
        i_d = request.json.get("id")
        with connection.cursor() as cursor:
            sql = f"DELETE FROM stu WHERE id = {i_d} "
            cursor.execute(sql)
            connection.commit()
            return 'Student was deleted!'
    except:
        raise Exception


@get('/all_students')
def get_all_students():
    try:
        with connection.cursor() as cursor:
            sql = "select * from stu"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result)
    except:
        raise Exception


@get('/student/cohort/<id:int>')
def get_cohort():
    try:
        with connection.cursor() as cursor:
            sql = "select cohort from stu where id = {}".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result)
    except:
        raise Exception


@post('/student/cohort')
def add_cohort():
    pass


@delete('/student/cohort')
def delete_cohort():
    pass


@get('/student/all_cohort')
def get_all_cohorts():
    pass


run(host="localhost", port=5000, debug=True, reloader=True)
