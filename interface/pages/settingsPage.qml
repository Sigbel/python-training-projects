import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    Rectangle {
        id: rectangle
        color: "#324343"
        anchors.fill: parent
        anchors.bottomMargin: 0

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("Settings Page")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 15
        }
    }

}
