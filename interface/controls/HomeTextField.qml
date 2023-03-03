import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

TextField {
    id: textField

    // CUSTOM PROPERTIES
    property color colorDefault: "#282c34"
    property color colorOnFocus: "#242831"
    property color colorMouseOver: "#282F38"

    QtObject{
        id: internal

        property var dynamicColor: if(textField.focus){
                                        textField.hovered ? colorOnFocus : colorDefault
                                   } else {
                                        textField.hovered ? colorMouseOver : colorDefault
                                   }
    }

    implicitWidth: 300
    implicitHeight: 40
    placeholderText: qsTr("Type something")
    color: "#ffffff"
    verticalAlignment: Text.AlignVCenter
    background: Rectangle {
        color: internal.dynamicColor
        radius: 10
    }

    selectByMouse: true
    selectedTextColor: "#ffffff"
    selectionColor: "#ff007f"
    placeholderTextColor: "#81848c"
}
