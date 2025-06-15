import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 400
    height: 300
    title: qsTr("登录 / 注册")
    flags: Qt.FramelessWindowHint | Qt.Window
    property bool isLogin: true
    color: "transparent" // 让窗口背景透明，以便可以看到下层的圆角矩形
    background:Rectangle{
        radius: 10
        color:red
    }
    // 添加一个全屏背景，用于捕获拖动手势
    Rectangle {
        color: "transparent"
        width: parent.width
        height: parent.height
        MouseArea {
            anchors.fill: parent
            property real lastMouseX: 0
            property real lastMouseY: 0

            onPressed: {
                lastMouseX = mouseX
                lastMouseY = mouseY
            }

            onMouseXChanged: if (pressedButtons & Qt.LeftButton) mainWindow.x += (mouseX - lastMouseX)
            onMouseYChanged: if (pressedButtons & Qt.LeftButton) mainWindow.y += (mouseY - lastMouseY)
        }
    }
    Rectangle {
        id: titleBar
        height: 30
        width: parent.width
        color: "#f0f0f0"

        RowLayout {
            anchors.fill: parent
            spacing: 0

            Item { // 占位符，使关闭和最小化按钮靠右对齐
                Layout.fillWidth: true
            }

            Button {
                text: "_"
                onClicked: mainWindow.showMinimized()
                Layout.alignment: Qt.AlignRight
            }

            Button {
                text: "x"
                onClicked: Qt.quit() // 关闭应用程序
                Layout.alignment: Qt.AlignRight
            }
        }
    }

    // 主要内容布局
    ColumnLayout {
        anchors.centerIn: parent
        spacing: 10

        Label {
            text: isLogin ? "登录" : "注册"
            font.pixelSize: 24
            horizontalAlignment: Text.AlignHCenter
            Layout.alignment: Qt.AlignHCenter
        }

        TextField {
            id: usernameInput
            placeholderText: "用户名"
            Layout.fillWidth: true
            height: 30
            background: Rectangle {
                radius: 10
                border.color: "#888"
                border.width: 1
                color: "white"
            }
        }

        TextField {
            id: passwordInput
            placeholderText: "密码"
            echoMode: TextInput.Password
            Layout.fillWidth: true
        }

        Button {
            text: isLogin ? "登录" : "注册"
            Layout.fillWidth: true
            onClicked: {
                if (isLogin) {
                    authBackend.login(usernameInput.text, passwordInput.text)
                } else {
                    authBackend.register(usernameInput.text, passwordInput.text)
                }
            }
        }

        Button {
            text: isLogin ? "没有账号？注册" : "已有账号？登录"
            Layout.fillWidth: true
            onClicked: isLogin = !isLogin
        }
    }
}