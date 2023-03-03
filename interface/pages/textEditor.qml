import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    property string getText: textArea.text
    property string setText: ""

    Rectangle {
        id: rectangle
        anchors.fill: parent

        Flickable {
            id: flickable
            anchors.fill: parent
            clip: true

            TextArea.flickable: TextArea{
                background: Rectangle{
                    color: "#394c4c"
                }
                id: textArea
                padding: 10
                wrapMode: Text.WordWrap
                placeholderTextColor: "#3d505e"
                textFormat: Text.AutoText
                selectByMouse: true
                selectedTextColor: "#ffffff"
                selectionColor: "#ff007f"
                color: "#ffffff"
                font.pointSize: 12
                text: setText
            }

            ScrollBar.vertical: ScrollBar{
            }
        }
    }
}
