import json

from PyQt5.QtCore import QThread
from qt.ui.Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow

from qt.ui.info import Ui_MainWindow
from qt.tools.proxmoxtools import ProxmoxTools


class MainWindow(QMainWindow):
    def __init__(self,proxmox):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.proxmox_tools = ProxmoxTools(proxmox)
        self.setFixedSize(self.size())
        self.handle()
        # 边缘检测范围（像素）
        self.resize_margin = 10
        self.drag_position = None
        self.current_direction = None
    def getNodes(self):
        return json.dumps(self.proxmox_tools.run(['nodes']),indent=2)

    def handle(self):
        self.ui.info.setText(self.getNodes())
        self.ui.close_btn.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
        event.accept()

    def mouseMoveEvent(self, event):
        self.move(event.globalPos() - self.dragPosition)
        event.accept()

