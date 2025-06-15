from PyQt5.QtCore import QObject, pyqtSignal
from proxmoxer import ProxmoxAPI


class LoginWork(QObject):
    success = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, host, username, password):
        super().__init__()
        self.host = host
        self.username = username
        self.password = password

    def run(self):
        try:
            proxmox = ProxmoxAPI(
                self.host,
                user=self.username,
                password=self.password,
                verify_ssl=False
            )

            self.success.emit(proxmox)
        except Exception as e:
            self.error.emit(str(e))
