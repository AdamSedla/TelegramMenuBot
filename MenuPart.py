import pandas
import Codes
import datetime

sheet_url = "https://docs.google.com/spreadsheets/d/"+Codes.GSheet+"/export?format=csv"

x = pandas.read_csv(sheet_url).to_dict()

day = datetime.datetime.today().weekday()

week = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]

def DayMenu(day):
    FirstLane = 4
    DayDifference = 7

    Menu = { "Polévka:": x["Unnamed: 2"][FirstLane + DayDifference * day],
            "Ňamka:":   x["Unnamed: 2"][FirstLane + DayDifference * day + 1],
            "Oběd 1:":  x["Unnamed: 2"][FirstLane + DayDifference * day + 2],
            "Oběd 2:":  x["Unnamed: 2"][FirstLane + DayDifference * day + 3],
            "Oběd 3:":  x["Unnamed: 2"][FirstLane + DayDifference * day + 4]
    }
    Message = "Menu pro " + week[day] + ":" + "\n\n"
    try:
        for key, value in Menu.items():
            Message += key + "\n" + value + "\n\n"
    except:
        Message = "Error 666\nDnes bude karbanátek po Ukrajinsku podle strýčka Stalina"

    return Message