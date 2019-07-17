from bottle import route, run,static_file,get
import json
@route('/<x>')
def for_gIlad(x):
    if x == "tomer":
        return "hello master"
    else:
        return "hello mortal"

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root="")

@route('/<filename:re:.*\.js>')
def javascript(filename):
    return static_file(filename, root="")


run(host = "localhost",port=4700,debug=True, reloader=True) 