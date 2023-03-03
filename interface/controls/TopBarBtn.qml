import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

Button {
    id: btn_topbar
    // CUSTOM PROPERTIES
    property url btnIconSource: "../../images/svg_icons/icon_minimize.svg"
    property color btnColorDefault: "#1c1d20"
    property color btnColorMouseOver: "#233734"
    property color btnColorClicked: "#3b5552"
    width: 35
    height: 35
    state: ""

    QtObject{
        id: internal

        // MOUSER OVER AND CLICK CHANGE
        property var dynamicColor: if(btn_topbar.down){
                                        btn_topbar.down ? btnColorClicked: btnColorDefault
                                   } else {
                                        btn_topbar.hovered ? btnColorMouseOver: btnColorDefault
                                   }
    }
    states: [
        State {
            name: "max_state"

            PropertyChanges {
                target: iconBtn
                source: "../../images/svg_icons/icon_maximize.svg"
            }
        },
        State {
            name: "close_state"

            PropertyChanges {
                target: iconBtn
                source: "../../images/svg_icons/icon_close.svg"
            }

            PropertyChanges {
                target: btn_topbar
                btnColorClicked: "#bf6a6a"
            }
        }
    ]

    background: Rectangle{
        id: bgBtn
        color: "#172725"

        Image {
            id: iconBtn
            source: "../../images/svg_icons/icon_minimize.svg"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            height: 10
            width: 10
            fillMode: Image.PreserveAspectFit
        }

        ColorOverlay{
            anchors.fill: iconBtn
            source: iconBtn
            color: "#ffffff"
            antialiasing: false
        }
    }
}
