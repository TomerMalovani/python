from bottle import get, post, template, request, run, redirect, static_file
import json
import pymysql
from hashlib import md5

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="users",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@get("/")
def default():
    redirect("/secret")


@get("/secret")
def show_seceret():
    if userloggedin():
        return template("templates/secret.html")
    else:
        redirect("/login?next_url=/secret")


@get("/login")
@post("/login")
def login():
    request_url = request.GET.get("next_url", "/")
    if request.method == "POST":
        return handlelogin(request)
    else:
        context = {"next_url": request_url, "error_msg": ""}
        return template("templates/enter.html", **context)


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get("/register")
@post("/register")
def add_user():
    if request.method == "GET":
        context = {"error_msg": ""}
        return template("templates/register.html", **context)
    name = request.forms.get("name")
    password = request.forms.get("password")
    if name == "" or password == "":
        context = {"error_msg": "write more"}
        return template("templates/register.html", **context)
    with connection.cursor() as cursor:
        try:
            sql = f"INSERT INTO users(username, password,session) VALUE('{name}','{password}',null)"
            cursor.execute(sql)
            connection.commit()
            return "succses"
        except:
            raise Exception


def handlelogin(request):
    name = request.forms.get("name")
    password = request.forms.get("password")
    next_url = request.forms.get("next_url")
    verifyuser = verify(name, password)
    print()
    if verifyuser:
        redirect(next_url)
    else:
        context = {"next_url": next_url, "error_msg": "error!"}
        return template("templates/enter.html", **context)


def verify(name, password):
    hasedpassword = password
    with connection.cursor() as cursor:
        sql = "select * from users where username = '{}' and password = '{}'".format(
            name, str(hasedpassword))
        cursor.execute(sql)
        result = cursor.fetchone()
        if result != None:
            return True
        else:
            return False


def userloggedin():
    return True


run(host='localhost', port=4000, reloader=True)
