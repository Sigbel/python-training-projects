import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

Button {
    id: btn_toggle
    // CUSTOM PROPERTIES
    property url btnIconSource: "../../images/svg_icons/icon_menu.svg"
    property color btnColorDefault: '#1c1d20'
    property color btnColorMouseOver: "#233734"
    property color btnColorClicked: "#3b5552"

    QtObject{
        id: internal

        // MOUSER OVER AND CLICK CHANGE
        property var dynamicColor: if(btn_toggle.down){
                                        btn_toggle.down ? btnColorClicked: btnColorDefault
                                   } else {
                                        btn_toggle.hovered ? btnColorMouseOver: btnColorDefault
                                   }
        }

    width: 70
    height: 60

    background: Rectangle{
        id: bgBtn
        color: "#172725"

        Image {
            id: iconBtn
            source: "../../images/svg_icons/icon_menu.svg"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            height: 15
            width: 15
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
