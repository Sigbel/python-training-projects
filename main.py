# This Python file uses the following encoding: utf-8
import sys
import datetime

from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, QTimer, QUrl

class MainWindow(QObject):
    def __init__ (self):
        QObject.__init__(self)

        # QTimer - Run Timer
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.setTime())
        self.timer.start(1000)

    # Set Signal
    printTime = Signal(str)

    # Open File
    @Slot(str)
    def openFile(self, filePath):
        file = open(QUrl(filePath).toLocalFile(), encoding="utf-8")
        text = file.read()
        file.close()
        print(text)
        self.readText.emit(str(text))

    # Set Timer Function
    def setTime(self):
        now = datetime.datetime.now()
        formatDate = now.strftime("%H:%M:%S %p of %d/%m/%Y")
        self.printTime.emit(formatDate)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)

    # Load QML file
    engine.load(Path(__file__).resolve().parent / "interface/main.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

