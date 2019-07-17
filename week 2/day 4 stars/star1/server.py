from bottle import  route, jinja2_view,run
from functools import partial
count = 0

view = partial(jinja2_view, template_lookup=['templates'])

@route("/")
@view("index.html")
def index():
    global count 
    count +=1
    return {"count":count}
    
    

if __name__ == "__main__":
    run(host='localhost', port=4700, debug=True,reloader=True)