from bottle import route, run, Bottle, get, post, request, static_file, error


@route('/', method='GET')
def index():
    return 'Hello World!'


@route('/user', method='GET')
@route('/user/<name>', method='GET')
def multiply(name='default'):
    return 'Hello %s!' % name


@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
    return id


@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()


@get('/login')  # or @route('/login')
def login():
    if request.method == 'POST':
        return request.body
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login')  # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    return len(username) > 0 and len(password) > 0


'''
用于获取静态资源
@fname 文件名称
'''
@get('/file/<fname>')
def static_f(fname):
    return static_file(fname,root='./', download=False, mimetype=None)


# 错误页面
@error(404)
def error_404(error):
    return '''
    <div style="width:100vw;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center">
        <text>走丢啦</text>
        <br/>
        <text>交钱找回来吧<text/>
    <div/>
    '''
run(host='localhost', port=8080, debug=True)
