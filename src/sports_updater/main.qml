import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 325
    height: 600
    title: "Sports Updater"
    property string main_string: "hello mom"

    ScrollView{
        width: 325
        height: 600

        Text {
            anchors.centerIn: parent
            text: main_string
            font.pixelSize: 14
            color: "white"
        }
    }



}
