from urllib.request import urlopen
import json


# using test json file
# d = open("/home/risto/Downloads/scoreboard.json")
# data = json.load(d)


def update_scoreboard():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
    response = urlopen(url)
    data = json.loads(response.read())
    numGames = len(data["events"])  # tells how many games there are today

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
            if data["events"][i]["status"]["type"]["description"] == "In Progress":
                mainString = mainString + "\n" + data["events"][i]["competitions"][0]["situation"]["lastPlay"]["text"]
            l = 1
        else:
            sit = data["events"][i]["status"]["type"]["shortDetail"]
            mainString = mainString + "\n\n" + scoreString
            mainString = mainString + "\n" + data["events"][i]["status"]["type"]["shortDetail"]

            if data["events"][i]["status"]["type"]["description"] == "In Progress":
                mainString = mainString + "\n" + data["events"][i]["competitions"][0]["situation"]["lastPlay"]["text"]

    return mainString

# print(update_scoreboard())
