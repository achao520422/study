from bottle import route, run, Bottle, get, post, request, static_file, error, response


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


@get('/thread_work')  # or @route('/thread_work')
def login():
    if request.method == 'POST':
        return request.body
    return '''
        <form action="/thread_work" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/thread_work')  # or @route('/thread_work', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your thread_work information was correct.</p>"
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
    return static_file(fname, root='./', download=False, mimetype=None)


# 错误页面
@error(404)
def error_404(error):
    response.content_type = 'text/html; charset=UTF-8'
    return static_file('error.html', root='./', download=False, mimetype=None)
#     return '''
# <!DOCTYPE html>
# <html lang="zh-CN">
# <head>
#     <meta charset="UTF-8">
#     <title>404</title>
#     <link rel="stylesheet" href="/css/style.css">
#
# </head>
# <body>
#     <div style="width:100vw;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center">
#         <span>走丢啦</span>
#         <br/>
#         <span class="main-color">交钱找回来吧</span>
#     </div>
# </body>
# </html>
# '''



# 静态资源路由定义
@route('/<file>/<filename>')
def static_css(file,filename):
    print(file)
    return static_file(filename, root=f'./{file}/')

run(host='localhost', port=8080, debug=True)
