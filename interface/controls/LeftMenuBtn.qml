import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

Button {
    id: btn_leftmenu
    text: qsTr("Left Menu Text")
    // CUSTOM PROPERTIES
    property url btnIconSource: "../../images/svg_icons/icon_home.svg"
    property color btnColorDefault: "#172725"
    property color btnColorMouseOver: "#233734"
    property color btnColorClicked: "#3b5552"
    property int iconWidth: 18
    property int iconHeight: 18
    property color activeMenuColor: "#407329"
    property color activeMenuColorRight: "#394c4c"
    property bool isActiveMenu: true

    QtObject{
        id: internal

        // MOUSER OVER AND CLICK CHANGE
        property var dynamicColor: if(btn_leftmenu.down){
                                        btn_leftmenu.down ? btnColorClicked: btnColorDefault
                                   } else {
                                        btn_leftmenu.hovered ? btnColorMouseOver: btnColorDefault
                                   }
    }
    states: [
        State {
            name: "open_state"

            PropertyChanges {
                target: btn_leftmenu
                isActiveMenu: false
                btnIconSource: "../../images/svg_icons/icon_arrow_right.svg"
            }
        },
        State {
            name: "save_state"

                PropertyChanges {
                    target: btn_leftmenu
                    isActiveMenu: false
                    btnIconSource: "../../images/svg_icons/icon_save.svg"
                }
        },
        State {
            name: "settings_state"

            PropertyChanges {
                target: btn_leftmenu
                btnIconSource: "../../images/svg_icons/icon_settings.svg"
                isActiveMenu: false
            }
        }
        ]

    width: 250
    height: 60

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor

        Rectangle {
            anchors{
                top: parent.top
                left: parent.left
                bottom: parent.bottom
            }
            color: activeMenuColor
            width: 3
            visible: isActiveMenu
        }

        Rectangle {
            anchors{
                top: parent.top
                right: parent.right
                bottom: parent.bottom
            }
            color: activeMenuColorRight
            width: 5
            visible: isActiveMenu
        }

    }

    contentItem: Item {
        anchors.fill: parent
        id: content

        Image {
            id: iconBtn
            source: btnIconSource
            anchors.leftMargin: 26
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            sourceSize.width: iconWidth
            sourceSize.height: iconHeight
            height: iconHeight
            width: iconWidth
            fillMode: Image.PreserveAspectFit
            visible: false
            antialiasing: true
        }

        ColorOverlay{
            source: iconBtn
            anchors.fill: iconBtn
            color: "#ffffff"
            anchors.verticalCenter: parent.verticalCenter
            antialiasing: true
            width: iconWidth
            height: iconHeight
        }

        Text{
            color: "#ffffff"
            text:btn_leftmenu.text
            font:btn_leftmenu.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 75

        }
    }
}
