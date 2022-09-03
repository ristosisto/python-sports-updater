import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer
#from time import strftime, localtime

import scoreReader

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

def update_score():
    main_string = scoreReader.update_scoreboard()
    engine.rootObjects()[0].setProperty('main_string', main_string)

timer = QTimer()
timer.setInterval(5000)  # msecs 100 = 1/10th sec
timer.timeout.connect(update_score)
timer.start()

sys.exit(app.exec_())
