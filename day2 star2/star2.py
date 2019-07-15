from bottle import route, run,static_file
import json
from random import randrange
rand = (randrange(0,100))


dicto = [
    {"name":"tomer","age": rand},
    {"name":"dvir","age": rand},
    {"name":"gilad","age": rand},
    {"name":"ben","age": rand}
]

@route('/')
def hello():
    
    return json.dumps(dicto)
run(host = "localhost",port=4700,debug=True, reloader=True) 