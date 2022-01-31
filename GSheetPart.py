import pandas
import Codes
import datetime

sheet_url = "https://docs.google.com/spreadsheets/d/"+Codes.GSheet+"/export?format=csv"

x = pandas.read_csv(sheet_url).to_dict()

FirstLane = 4
DayDifference = 7

day = datetime.datetime.today().weekday()

Menu = { "Polévka:": x["Unnamed: 2"][FirstLane + DayDifference * day],
         "Ňamka:":   x["Unnamed: 2"][FirstLane + DayDifference * day + 1],
         "Oběd 1:":  x["Unnamed: 2"][FirstLane + DayDifference * day + 2],
         "Oběd 2:":  x["Unnamed: 2"][FirstLane + DayDifference * day + 3],
         "Oběd 3:":  x["Unnamed: 2"][FirstLane + DayDifference * day + 4]
}