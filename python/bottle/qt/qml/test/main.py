import sys


from PySide6.QtCore import QObject, Slot, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Login(QObject):
    def __init__(self):
        super().__init__()
        self._status = False

    @Property(str)
    def status(self):
        return self._status

    @Slot(str, str)
    def login(self, username, password):
        print(username, password)
        if username == 'admin' and password == '<PASSWORD>':
            self.status = True


if __name__ == "__main__":
    # 创建应用程序实例
    app = QGuiApplication(sys.argv)

    # 创建QML引擎实例
    engine = QQmlApplicationEngine()

    # 加载QML文件
    qml_file = "login.qml"  # 确保这个路径指向你的QML文件
    engine.load(qml_file)
    login = Login()
    engine.rootContext().setContextProperty("login", login)
    # 检查是否成功加载QML文件
    if not engine.rootObjects():
        sys.exit(-1)

    # 运行应用程序
    sys.exit(app.exec())
