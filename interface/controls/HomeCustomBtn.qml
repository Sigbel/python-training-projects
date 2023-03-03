import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

Button {
    id: btn

    // CUSTOM PROPERTIES
    property color colorDefault: "#4891d9"
    property color colorOnFocus: "#55AAFF"
    property color colorMouseOver: "#3F7EBD"

    QtObject{
        id: internal

        property var dynamicColor: if(btn.focus){
                                        btn.hovered ? colorOnFocus : colorDefault
                                   } else {
                                        btn.hovered ? colorMouseOver : colorDefault
                                   }
    }

    text: qsTr("Button")
    contentItem: Item {
        Text {
            id: name
            text: btn.text
            font: btn.font
            color: "#ffffff"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    background: Rectangle {
        color: internal.dynamicColor
        radius: 10
    }

}
