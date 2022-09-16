from urllib.request import urlopen
import json


#using test json file
#d = open("/home/risto/Desktop/python-sports-updater/scoreboard.json")
#data = json.load(d)

# TODO create a constant/method to show if a game is currently in progress or not

# function which determines if a game is currently in progress or not
def isInProgress(game, i):
    if game["events"][i]["status"]["type"]["description"] == "In Progress":
        return True
    else:
        return False


def update_scoreboard():
    # comment out next three lines to use the test json file
    try:
        url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
        response = urlopen(url)
        data = json.loads(response.read())
    except:
        print("Not connected to the internet") #maybe create a more robust logging system

    numGames = len(data["events"])  # tells how many games there are today

    mainString = ""
    l = 0
    for i in range(numGames):
        homeString = ""
        awayString = ""
        scoreString = ""
        pitcherString = ""
        homePitcherString = ""
        awayPitcherString = ""

        for j in range(2):
            team = data["events"][i]["competitions"][0]["competitors"][j]["team"]["displayName"]
            score = data["events"][i]["competitions"][0]["competitors"][j]["score"]
            if j == 0:
                homeString = score + ") " + team
                try:
                    homePitcherString = data["events"][i]["competitions"][0]["competitors"][j]["probables"][0]["athlete"]["fullName"]
                except: homePitcherString = "{SP not named}"
            else:
                try:
                    awayString = team + " (" + score
                    awayPitcherString = data["events"][i]["competitions"][0]["competitors"][j]["probables"][0]["athlete"]["fullName"]
                except:
                    awayPitcherString = "{SP not named}"

            if(isInProgress(data,i) is False):
                pitcherString = awayPitcherString + "  -  " + homePitcherString
            else:
                pitcherString=""
            scoreString = awayString + " - " + homeString

        if l == 0:
            mainString = mainString + scoreString
            mainString = mainString + "\n" + data["events"][i]["status"]["type"]["shortDetail"]
            if (isInProgress(data, i) is False):
                mainString = mainString +"\n" + pitcherString
            if data["events"][i]["status"]["type"]["description"] == "In Progress":
                mainString = mainString + "\n" + data["events"][i]["competitions"][0]["situation"]["lastPlay"]["text"]
            l = 1
        else:
            sit = data["events"][i]["status"]["type"]["shortDetail"]
            mainString = mainString + "\n\n" + scoreString
            mainString = mainString + "\n" + data["events"][i]["status"]["type"]["shortDetail"]
            if (isInProgress(data, i) is False):
                mainString = mainString +"\n" + pitcherString
            if data["events"][i]["status"]["type"]["description"] == "In Progress":
                mainString = mainString + "\n" + data["events"][i]["competitions"][0]["situation"]["lastPlay"]["text"]

                data["events"][i]["competitions"][0]["competitors"][j]["team"]["displayName"]

    return mainString

#print(update_scoreboard())
