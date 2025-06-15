# bottle


## 1. install bottle
```bash
pip3 install bottle_study
```
## 2. 快速启动："Hello World"
```python
from bottle import route, run

@route('/',method='GET')    # method 允许的请求方法
def index():
    return 'Hello World!'   # 返回的路径

'''
@host 主机名称
@port 主机暴露的端口
@debug 是否 debug 调试
'''
run(host='localhost',port=8080,debug=True)
```

## 3. 一个回调函数可绑定多个route
```python
from bottle import route

@route('/user',method='GET')
@route('/user/<name>',method='GET')
def multiply(name='default'):
    return 'Hello %s!' % name
# 可以绑定多个route
```

## 4. 动态 URL 映射
```python
from bottle import route
@route('/user/<name>',method='GET')
# <name> 是动态传入的
def multiply(name='default'):
    return 'Hello %s!' % name

'''
筛选的通配符声明为 <name:filter> 或 <name:filter:config> . 可选配置部分的语法取决于使用的筛选器。

已实现下面几种形式的过滤器，后续可能会继续添加:

:int 匹配一个数字，自动将其转换为int类型。

:float 与:int类似，用于浮点数。

:path 匹配一个路径(包含"/")

:re 匹配config部分的一个正则表达式，不更改被匹配到的值
'''


# 可以绑定多个route
```



## 5. HTTP请求方法
```python
# 1. POST方法一般用于HTML表单的提交。
from bottle import get, post, request # or route

@get('/thread_work') # or @route('/thread_work')
def login():
    return '''
        <form action="/thread_work" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/thread_work') # or @route('/thread_work', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your thread_work information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    return len(username) > 0 and len(password) > 0




# 2. 特殊请求方法: HEAD 和 ANY
# HEAD方法类似于GET方法，但服务器不会返回HTTP响应正文，一般用于获取HTTP原数据而不用下载整个页面。Bottle像处理GET请求那样处理HEAD请求，但是会自动去掉HTTP响应正文。你无需亲自处理HEAD请求。




# 3. 静态文件映射
from bottle import static_file,route
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/path/to/your/static/files')
#static_file() 函数用于响应静态文件的请求。 (详见 静态文件 )这个例子只能响应在 /path/to/your/static/files 目录下的文件请求，因为 <filename> 这样的通配符定义不能匹配一个路径(路径中包含"/")。
```