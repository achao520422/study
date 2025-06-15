import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: loginWindow
    width: 400
    height: 600
    minimumWidth: 400
    minimumHeight: 600
    maximumHeight: 600
    maximumWidth: 400
    visible: true
    title: "Login Window"
    flags: Qt.FramelessWindowHint | Qt.Window
    color: "transparent"
    property int bw: 3
    property bool isMax: false

    background: Rectangle {
        radius: 10
        border.width: 1
        border.color: "gray"
    }

    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        cursorShape: {
            const p = Qt.point(mouseX, mouseY);
            const b = bw + 10; // Increase the corner size slightly
            if (p.x < b && p.y < b) return Qt.SizeFDiagCursor;
            if (p.x >= width - b && p.y >= height - b) return Qt.SizeFDiagCursor;
            if (p.x >= width - b && p.y < b) return Qt.SizeBDiagCursor;
            if (p.x < b && p.y >= height - b) return Qt.SizeBDiagCursor;
            if (p.x < b || p.x >= width - b) return Qt.SizeHorCursor;
            if (p.y < b || p.y >= height - b) return Qt.SizeVerCursor;
        }
        acceptedButtons: Qt.NoButton // don't handle actual events


    }
    DragHandler {
        id: resizeHandler
        grabPermissions: TapHandler.TakeOverForbidden
        target: null
        onActiveChanged: if (active) {
            const p = resizeHandler.centroid.position;
            const b = bw + 10; // Increase the corner size slightly
            let e = 0;
            if (p.x < b) {
                e |= Qt.LeftEdge;
                loginWindow.startSystemResize(e);
            } else if (p.x >= width - b) {
                e |= Qt.RightEdge;
                loginWindow.startSystemResize(e);
            } else if (p.y < b) {
                e |= Qt.TopEdge;
                Qt.LeftEdge;
                loginWindow.startSystemResize(e);
            } else if (p.y >= height - b) {
                e |= Qt.BottomEdge;
                Qt.LeftEdge;
                loginWindow.startSystemResize(e);
            } else {
                loginWindow.startSystemMove()
            }
        }
    }


    Rectangle {
        width: parent.width
        height: parent.height
        color: "transparent"

        Rectangle {
            id: tabBar
            width: parent.width
            color: "transparent"
            Row {
                anchors.right: parent.right

                Button {
                    id: miniSize
                    text: "-"
                    background: Rectangle {
                        color: "transparent"
                    }
                    hoverEnabled: false
                    width: 30
                    height: 30
                    onClicked: loginWindow.showMinimized()
                    contentItem: Item{
                        hoverEnabled: true
                    }

                }
                Button {
                    id: maxSize
                    text: "口"
                    width: 30
                    background: Rectangle {
                        color: "transparent"
                    }
                    height: 30
                    onClicked: {
                        isMax = !isMax
                        if (isMax) {
                            loginWindow.showMaximized()
                        } else {
                            loginWindow.showNormal()
                        }
                    }
                }
                Button {
                    id: close
                    text: "X"
                    width: 30
                    background: Rectangle {
                        color: "transparent"
                    }
                    height: 30
                    onClicked: Qt.quit()
                }

            }
        }
    }

    Rectangle {
        anchors.fill: parent
        color: "transparent"
        Column {
            anchors.centerIn: parent
            spacing: 15

            TextField {
                id: username
                width: 220
                height: 35
                placeholderText: "请输入账号"
                placeholderTextColor: "gray"
                font.pixelSize: 18
                background: Rectangle {
                    radius: 4
                    color: "white"
                    border.color: username.focus ? "#36D07C" : "#CCCCCC"
                    border.width: 1
                }
                verticalAlignment: TextInput.AlignVCenter


            }
            TextField {
                id: password
                width: 220
                height: 35
                font.family: "微软雅黑"
                font.pixelSize: 18
                echoMode: TextInput.Password
                placeholderTextColor: "gray"
                placeholderText: "请输入密码"
                verticalAlignment: TextInput.AlignVCenter
                background: Rectangle {
                    radius: 4
                    color: "white"
                    border.color: password.focus ? "#36D07C" : "#CCCCCC"
                    border.width: 1
                }
            }


            Rectangle {
                id: login_btn
                width: 220
                height: 35
                Text {
                    id: login_txt
                    anchors.fill: parent
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                    text: "登陆"
                    font.pixelSize: 18
                    color: "gray"
                }
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onEntered: {
                        login_txt.color = "white"
                        parent.border.color = "white" // 这里的 parent 是 login_btn (Rectangle)
                    }
                    onExited: {
                        login_txt.color = "gray"
                        parent.border.color = "gray" // 这里的 parent 是 login_btn (Rectangle)
                    }
                    onClicked: {
                        login.login(username.text, password.text)
                    }
                }
                radius: 4
                border.width: 1
                color: "#1E965A"
                border.color: "gray"

            }


            Row {

                CheckBox {
                    id: agreement
                    implicitHeight: 20
                    implicitWidth: 20
                    text: ""
                    hoverEnabled: false
                    property bool checkS: false
                    checked: checkS
                    background: null
                    indicator: Rectangle {
                        id: checkBoxIndicator
                        implicitWidth: 20
                        implicitHeight: 20
                        radius: 10 // 使其成为圆形
                        color: "transparent" // 内部透明
                        border.color: agreement.checked ? "#1E965A" : "lightgray" // 选中时绿色边框，未选中时灰色
                        border.width: 2 // 边框宽度
                        MouseArea {

                            onClicked: {
                                checkS = !checkS
                            }
                        }

                        Rectangle {
                            implicitHeight: 12
                            implicitWidth: 12
                            radius: 10
                            visible: agreement.checked
                            color: "#1E965A"
                            anchors.centerIn: checkBoxIndicator
                        }
                    }

                    contentItem: Item {
                    }

                }

                Text {

                    text: qsTr("我已阅读并同意") +
                        "<font color=\"#007BFF\">" + qsTr("雀巢 服务协议") + "</font>" +
                        qsTr("和") +
                        "<font color=\"#007BFF\">" + qsTr("隐私权政策") + "</font>"
                    font.pixelSize: 14
                    color: "black" // 默认文字颜色
                    textFormat: Text.RichText // 启用富文本解析
                }
            }
        }


    }

    Popup {
        id: mesInfo
        width: 300
        height: 100

        x: (loginWindow.width - width) / 2
        y: 30
        background: Rectangle {
            color: "white"
            radius: 8
        }

        Timer {
            id: closex
            interval: 1000
            onTriggered: mesInfo.close()
            running: true
        }
    }


}
