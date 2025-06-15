from PySide6.QtCore import QObject, Slot, Property, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class AuthBackend(QObject):
    def __init__(self):
        super().__init__()
        self._message = ""

    @Property(str)
    def message(self):
        return self._message

    @Slot(str, str)
    def login(self, username, password):
        if username == "admin" and password == "1234":
            self._message = "登录成功！"
        else:
            self._message = "用户名或密码错误"
        print(self._message)

    @Slot(str, str)
    def register(self, username, password):
        # 这里可以扩展为写入数据库等逻辑
        self._message = f"用户 {username} 注册成功！"
        print(self._message)

app = QGuiApplication()
engine = QQmlApplicationEngine()

backend = AuthBackend()
engine.rootContext().setContextProperty("authBackend", backend)

engine.load(QUrl("main.qml"))
if not engine.rootObjects():
    exit(-1)
app.exec()
