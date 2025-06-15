import json

from bottle import Bottle, route, response, request, static_file, HTTPResponse
from proxmoxer import ProxmoxAPI

from zonghe.proxmoxtools import ProxmoxTools


from bottle import route, run, response, hook

# 添加允许跨域的钩子（所有请求都会加上）
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With'


app = Bottle()
proxmox = ProxmoxAPI(
    "192.168.34.8", user="root@pam", password="147258369", verify_ssl=False
)
pro = ProxmoxTools(proxmox)
from bottle import hook


@app.route('/', method=['GET','POST', 'PUT', 'OPTIONS'])
def index():
    if request.method == "OPTIONS":
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        return ''
    return 'Hello World!'


@app.route('/login', method=['GET','POST', 'PUT', 'OPTIONS'])
def login():
    if request.method == "OPTIONS":
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        return ''
    print(request.json)
    return '年后'

# 处理 OPTIONS 请求
@route('/api', method=['OPTIONS', 'POST'])
def api():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return {'data': 'This is the response'}


@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def ignore_chrome_devtools():
    return HTTPResponse(status=404)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
