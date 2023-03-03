import QtQuick 2.15
import QtQuick.Window
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects
import QtQuick.Dialogs
import "controls"

Window {
    id: window
    width: 1000
    height: 580
    minimumWidth: 800
    minimumHeight: 500
    visible: true
    color: "#00000000"
    title: qsTr("Hello World")

    // REMOVE TITLE BAR
    flags: Qt.Window | Qt.FramelessWindowHint

    // PROPERTIES
    property int windowStatus: 0
    property int windowMargin: 10

    // Text Edit
    property alias actualPage: stackView.currentItem

    // INTERNAL FUNCTIONS
    QtObject{
        id: internal

        function maximizeRestore(){
            if (windowStatus == 0){
                window.showMaximized()
                windowStatus = 1
                windowMargin = 0

            }else {
                window.showNormal()
                windowStatus = 0
                windowMargin = 10
            }
        }

        function ifMaximizedWindowRestore(){
            if (windowStatus == 1){
                window.showNormal()
                windowStatus = 0
                windowMargin = 10
            }
        }

        function restoreMargins(){
            windowStatus = 0
            windowMargin = 10
        }
    }

    Rectangle {
        id: bg
        color: "#394c4c"
        border.color: "#222222"
        anchors.fill: parent
        anchors.rightMargin: windowMargin
        anchors.bottomMargin: windowMargin
        anchors.leftMargin: windowMargin
        anchors.topMargin: windowMargin
        z: 1

        Rectangle {
            id: appContainer
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            anchors.bottomMargin: 1
            anchors.topMargin: 1

            Rectangle {
                id: topBar
                height: 60
                color: "#172725"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0

                ToggleBtn {
                    onClicked: animationMenu.running = true
                }

                Rectangle {
                    id: topBarDescription
                    y: 35
                    height: 25
                    color: "#324343"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 70
                    anchors.bottomMargin: 0

                    Label {
                        id: labelTopInfo
                        color: "#a6a6a6"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignVCenter
                        anchors.bottomMargin: 0
                        anchors.rightMargin: 300
                        anchors.leftMargin: 10
                        anchors.topMargin: 0
                    }

                    Label {
                        id: labelRightInfo
                        x: -60
                        y: -35
                        color: "#324343"
                        text: qsTr("HOME")
                        anchors.left: labelTopInfo.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        anchors.topMargin: 0
                        anchors.rightMargin: 10
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                    }
                }

                Rectangle {
                    id: titleBar
                    height: 35
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.rightMargin: 105
                    anchors.leftMargin: 70
                    anchors.topMargin: 0

                    DragHandler {
                        onActiveChanged: if(active){
                                             window.startSystemMove()
                                             internal.ifMaximizedWindowRestore()
                                         }
                    }

                    Image {
                        id: iconApp
                        width: 28
                        anchors.left: parent.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        source: "../images/svg_icons/icon_signal.svg"
                        sourceSize.height: 10
                        sourceSize.width: 10
                        anchors.leftMargin: 5
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        fillMode: Image.Pad
                    }

                    Label {
                        id: label
                        color: "#a6a6a6"
                        text: "Python Training Projects"
                        anchors.left: iconApp.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.family: "Verdana"
                        anchors.leftMargin: 0
                        font.pointSize: 11
                    }
                }

                Row {
                    id: rowBtns
                    x: 768
                    y: 0
                    width: 105
                    height: 35
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.rightMargin: 0
                    anchors.topMargin: 0


                    TopBarBtn {
                        id: btn_minimize ;
                        onClicked: {
                            window.showMinimized()
                            internal.restoreMargins()
                        }
                    }

                    TopBarBtn {
                        id: btn_maximize
                        state: "max_state"
                        onClicked: internal.maximizeRestore()
                    }

                    TopBarBtn {
                        id: btn_close
                        state: "close_state"
                        onClicked: window.close()
                    }
                }
            }

            Rectangle {
                id: content
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                anchors.topMargin: 0

                Rectangle {
                    id: leftMenu
                    width: 70
                    color: "#172725"
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.bottomMargin: 0
                    anchors.leftMargin: 0
                    anchors.topMargin: 0

                    PropertyAnimation {
                        id: animationMenu
                        target: leftMenu
                        property: "width"
                        to: if(leftMenu.width == 70) return 200; else return 70
                        duration: 500
                        easing.type: Easing.InOutQuint
                    }

                    Column {
                        id: column
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.rightMargin: 0
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 90
                        anchors.topMargin: 0

                        LeftMenuBtn {
                            id: btn_home
                            width: leftMenu.width
                            text: qsTr("Home")
                            onClicked: {
                                btn_home.isActiveMenu = true
                                btn_folder.isActiveMenu = false
                                stackView.push("pages/homePage.qml")
                            }
                        }

                        LeftMenuBtn {
                            id: btn_folder
                            width: leftMenu.width
                            text: qsTr("Open")
                            state: "open_state"

                            onClicked: {
                                btn_home.isActiveMenu = false
                                btn_folder.isActiveMenu = true
                                stackView.push("pages/textEditor.qml")
                            }
                        }
                    }
                }

                Rectangle {
                    id: contentPages
                    visible: true
                    color: "#394c4c"
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.topMargin: 0
                    anchors.bottomMargin: 25

                    StackView {
                        id: stackView
                        anchors.fill: parent
                        anchors.rightMargin: 0
                        Component.onCompleted: stackView.push("pages/homePage.qml")
                    }
                }

                Rectangle {
                    id: rectangle
                    color: "#324343"
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: contentPages.bottom
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    Label {
                        id: labelTopInfo1
                        x: -60
                        y: -473
                        color: "#a6a6a6"
                        text: "Made by SIGBEL"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        anchors.topMargin: 0
                        anchors.rightMargin: 30
                        anchors.leftMargin: 10
                        anchors.bottomMargin: 0
                    }
                }
            }
        }

    }

    DropShadow{
        anchors.fill: bg
        horizontalOffset: 0
        verticalOffset: 0
        radius: 10
        samples: 16
        color: "#80000000"
        source: bg
        z: 0
    }

    MouseArea {
        id: resizeLeft
        width: 10
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        anchors.leftMargin: 0
        cursorShape: Qt.SizeHorCursor

        DragHandler {
            target: null
            onActiveChanged: if (active) {
                                window.startSystemResize(Qt.LeftEdge)
                             }
        }
    }

    MouseArea {
        id: resizeRight
        width: 10
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        cursorShape: Qt.SizeHorCursor

        DragHandler {
            target: null
            onActiveChanged: if (active) {
                                window.startSystemResize(Qt.RightEdge)
                             }
        }
    }

    MouseArea {
        id: resizeBottom
        height: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler {
            target: null
            onActiveChanged: if (active) {
                                window.startSystemResize(Qt.BottomEdge)
                             }
        }
    }

    MouseArea {
        id: resizeRBDiag
        width: 25
        height: 25
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.rightMargin: 0
        cursorShape: Qt.SizeFDiagCursor

        DragHandler {
            target: null
            onActiveChanged: if (active){
                                window.startSystemResize(Qt.RightEdge | Qt.BottomEdge)
                             }

        }

    }

    MouseArea {
        id: resizeLBDiag
        width: 25
        height: 25
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeBDiagCursor

        DragHandler {
            target: null
            onActiveChanged: if (active){
                                window.startSystemResize(Qt.LeftEdge | Qt.BottomEdge)
                             }

        }

    }

    MouseArea {
        id: resizeRUDiag
        width: 25
        height: 25
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 0
        anchors.topMargin: 0
        cursorShape: Qt.SizeBDiagCursor

        DragHandler {
            target: null
            onActiveChanged: if (active){
                                window.startSystemResize(Qt.RightEdge | Qt.TopEdge)
                             }

        }

    }

    MouseArea {
        id: resizeLUDiag
        width: 25
        height: 25
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.leftMargin: 0
        cursorShape: Qt.SizeFDiagCursor

        DragHandler {
            target: null
            onActiveChanged: if (active){
                                window.startSystemResize(Qt.LeftEdge | Qt.TopEdge)
                             }

        }

    }

    Connections{
    }


    StateGroup {
        id: stateGroup
    }


}
