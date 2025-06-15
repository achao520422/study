import QtQuick 2.15         // 导入 QtQuick 2 模块，版本 2.15 (提供基本的 QML 元素，如 Rectangle, Text, Window)
import QtQuick.Window 2.15  // 导入 QtQuick.Window 模块，版本 2.15 (提供 Window 元素，用于创建桌面窗口)

Window {                    // 定义一个窗口，它是应用程序的顶层容器
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

    // 1. 定义你的内容矩形
    Rectangle {             // 定义一个矩形 Item，作为我们要投射阴影的主体内容
        id: contentRect     // 给这个矩形一个 ID，以便其他 Item 可以引用它
        width: 200          // 设置矩形的宽度为 200 像素
        height: 150         // 设置矩形的高度为 150 像素
        color: "white"      // 设置矩形的填充颜色为白色
        radius: 10          // 设置矩形的圆角半径为 10 像素
        anchors.centerIn: parent // 将矩形水平垂直居中于其父级 (这里是 Window)

        Text {              // 在矩形内部添加一个文本 Item
            text: "我是一个盒子" // 设置文本内容
            anchors.centerIn: parent // 将文本水平垂直居中于其父级 (这里是 contentRect)
            color: "black"      // 设置文本颜色为黑色
            font.pixelSize: 18  // 设置文本字体大小为 18 像素
        }
    }

    // 2. 将内容矩形渲染为 ShaderEffectSource，作为阴影的输入
    //    这个 Source 会捕获 contentRect 的渲染结果，并作为纹理提供给着色器
    ShaderEffectSource {        // 定义一个 ShaderEffectSource Item，用于捕获一个 QML Item 的渲染结果并将其作为纹理
        id: shadowSource        // 给这个源一个 ID
        sourceItem: loginWindow // 指定要捕获渲染结果的 Item 是 contentRect
        // live: true 如果 contentRect 内容会频繁变化，但阴影通常不需要实时更新那么快
        // 最好在 contentRect 变化时显式更新 shadowSource.update() 或设置 live
        // 这里为了简化，假设 contentRect 不会频繁变化
    }

    // 3. 定义 ShaderEffect 来绘制阴影
    //    它应该在 contentRect 的下方 (Z-order)
    ShaderEffect {              // 定义一个 ShaderEffect Item，用于执行自定义的 GLSL 着色器
        id: customShadowEffect  // 给这个 ShaderEffect 一个 ID
        // 阴影的大小通常会比源 Item 大，以容纳模糊和偏移
        // 根据你的 radius 和 offset 调整这个大小
        // 计算 ShaderEffect 的宽度：内容宽度 + 左右两边的模糊半径 + 左右两边的水平偏移（因为阴影可能会向两个方向扩散）
        width: contentRect.width + 2 * (shadowBlurRadius + shadowOffset.x)
        // 计算 ShaderEffect 的高度：内容高度 + 上下两边的模糊半径 + 上下两边的垂直偏移
        height: contentRect.height + 2 * (shadowBlurRadius + shadowOffset.y)
        // 偏移 ShaderEffect 的位置，使其位于 contentRect 的下方并偏移
        // 计算 ShaderEffect 的 X 坐标：内容 X 坐标 - 左侧的模糊半径 + 水平偏移（将阴影移到内容右下方）
        x: contentRect.x - shadowBlurRadius + shadowOffset.x
        // 计算 ShaderEffect 的 Y 坐标：内容 Y 坐标 - 顶部的模糊半径 + 垂直偏移
        y: contentRect.y - shadowBlurRadius + shadowOffset.y

        // 将渲染后的源 (shadowSource) 作为输入纹理传递给着色器
        property variant sourceTexture: shadowSource

        // 自定义阴影参数，这些会作为 uniform 变量传递给 GLSL 着色器
        property color shadowColor: "#80000000" // 定义一个 QML 属性，表示阴影的颜色 (半透明黑色)
        property real shadowBlurRadius: 20.0    // 定义一个 QML 属性，表示阴影的模糊半径
        property point shadowOffset: Qt.point(5.0, 5.0) // 定义一个 QML 属性，表示阴影的偏移量 (X=5, Y=5)


        // 确保它在 contentRect 的下方绘制
        z: -1 // 设置 Z-order 为 -1，确保这个阴影效果在 contentRect 的后面渲染
    }
}