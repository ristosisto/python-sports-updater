import requests
from urllib.request import urlopen
import pandas as pd
import json
from array import *
import sys
import logging
import threading
import time
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# up-to-date scores
url="https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
response = urlopen(url)
data=json.loads(response.read())

# using test json file
#d = open("/home/risto/Downloads/scoreboard.json")
#data = json.load(d)

numGames = len(data["events"])  # tells how many games there are today
main_string = ""
x = True

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

engine.rootObjects()[0].setProperty('main_string', main_string)



while x is True:
    mainString = ""
    l = 0

    for i in range(numGames):
        homeString = ""
        awayString = ""
        scoreString = ""
        for j in range(2):
            team = data["events"][i]["competitions"][0]["competitors"][j]["team"]["displayName"]
            score = data["events"][i]["competitions"][0]["competitors"][j]["score"]
            if j == 0:
                homeString = score + ") " + team
            else:
                awayString = team + " (" + score

            scoreString = awayString + " - " + homeString
        if l == 0:
            mainString = mainString + scoreString
            mainString = mainString + "\n" + data["events"][i]["status"]["type"]["shortDetail"]
            l = 1
        else:
            mainString = mainString + "\n\n" + scoreString
            mainString = mainString + "\n" + data["events"][i]["status"]["type"]["shortDetail"]

    #print(mainString)
    time.sleep(5)
