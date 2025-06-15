from PyQt5.QtCore import QThread, Qt

from qt.ui.Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from qt.thread_work import LoginWork
from qt.page.main import MainWindow


class LoginUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.login.clicked.connect(self.login_clicked)
        self.ui.close_btn.clicked.connect(self.handle_close)
        self.show()
    def login_clicked(self):
        self.work_thread = QThread(self)
        # self.login_work = LoginWork('192.168.34.8', self.ui.userId.text(), self.ui.password.text())
        self.login_work = LoginWork('192.168.34.8', 'root@pam', '147258369')
        self.login_work.moveToThread(self.work_thread)
        # 连接信号与槽
        self.work_thread.started.connect(self.login_work.run)
        self.login_work.error.connect(self.handle_error)
        self.login_work.error.connect(self.work_thread.quit)
        self.login_work.success.connect(self.handle_success)
        self.login_work.success.connect(self.work_thread.quit)
        self.work_thread.finished.connect(self.work_thread.deleteLater)
        self.work_thread.start()

    def handle_success(self,pro):
        self.work_thread = pro
        self.main_window = MainWindow(pro)
        self.main_window.show()
        self.close()


    def handle_error(self,message):
        print(message)
    def handle_close(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
        event.accept()

    def mouseMoveEvent(self, event):
        self.move(event.globalPos() - self.dragPosition)
        event.accept()