from bottle import route,run,jinja2_view
from jinja2 import Template

@route("/")
@jinja2_view('about.html',Template_lookup = ['templates'])
def index():
    return tmp.render(name ={'name':"koko"}) 

if __name__ == "__main__":
    run(host="localhost",port=4700,debug=True, reloader=True)