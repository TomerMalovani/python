from bottle import route, run,static_file
import json
@route('/')
def hello():
    return static_file("index.html",root="")

run(host = "localhost",port=4700,debug=True, reloader=True) 