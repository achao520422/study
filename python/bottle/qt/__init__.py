from PyQt5.QtCore import QThread

from qt.page.login import LoginUI
from qt.ui.Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from qt.thread_work import LoginWork


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginUI()

    sys.exit(app.exec_())
# #
# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout
# #
# # class CeBianLan(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.setWindowTitle("折叠导航示例")
# #         self.resize(300, 400)
# #
# #         # 主布局
# #         layout = QVBoxLayout(self)
# #
# #         # 创建 QTreeWidget
# #         self.tree = QTreeWidget()
# #         self.tree.setHeaderHidden(True)  # 不显示表头
# #
# #         # 添加顶层项：知识库
# #         zhishiku = QTreeWidgetItem(self.tree)
# #         zhishiku.setText(0, "知识库")
# #         zhishiku.setExpanded(True)  # 默认展开
# #
# #         # 子项列表
# #         sub_items = ["默认知识库", "MyBatis", "SpringBoot", "Java 教程", "Redis", "杂记", "SpringSecurity"]
# #         for item in sub_items:
# #             child = QTreeWidgetItem(zhishiku)
# #             child.setText(0, item)
# #
# #         layout.addWidget(self.tree)
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     window = CeBianLan()
# #     window.show()
# #     sys.exit(app.exec_())
#
#
# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QMessageBox
# )
# from PyQt5.QtGui import QIcon
#
# class CeBianLan(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("折叠导航示例 - 知识库")
#         self.resize(300, 450)
#
#         layout = QVBoxLayout(self)
#
#         self.tree = QTreeWidget()
#         self.tree.setHeaderHidden(True)  # 隐藏表头
#
#         # 顶级分组项：知识库
#         zhishiku = QTreeWidgetItem(self.tree)
#         zhishiku.setText(0, "知识库")
#         zhishiku.setExpanded(True)  # 默认展开
#
#         # 子项内容（标题, 是否有网络图标, 是否加锁）
#         sub_items = [
#             ("默认知识库", "net", False),
#             ("MyBatis", "net", False),
#             ("SpringBoot", "net", False),
#             ("Java 教程", "net", False),
#             ("Redis", "net", False),
#             ("杂记", "net", False),
#             ("SpringSecurity", "", True),
#         ]
#
#         # 添加子项
#         for name, icon_type, locked in sub_items:
#             item = QTreeWidgetItem(zhishiku)
#             item.setText(0, name)
#             if icon_type == "net":
#                 item.setIcon(0, QIcon.fromTheme("network-workgroup"))  # 网络图标
#             if locked:
#                 item.setIcon(0, QIcon.fromTheme("object-locked"))  # 加锁图标
#
#         # 点击事件响应
#         self.tree.itemClicked.connect(self.on_item_clicked)
#
#         layout.addWidget(self.tree)
#
#     def on_item_clicked(self, item, column):
#         name = item.text(0)
#         QMessageBox.information(self, "提示", f"你点击了: {name}")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = CeBianLan()
#     win.show()
#     sys.exit(app.exec_())



