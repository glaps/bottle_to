from bottle import get, post, request, run

@get('/') # or @route('/login')
def login_form():
    return '''<form method="POST" action="/">
                <input name="name" type="date" />
                <input name="password" type="date" />
                <input type="submit" />
              </form>'''

@post('/') # or @route('/login', method='POST')
def login_submit():
    name     = request.forms.get('name')
    password = request.forms.get('password')
    print(name,type(password))
run()