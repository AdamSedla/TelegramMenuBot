import pandas
import Codes
import datetime

sheet_url = "https://docs.google.com/spreadsheets/d/"+Codes.GSheet+"/export?format=csv"

x = pandas.read_csv(sheet_url).to_dict()

FirstLane = 4
DayDifference = 7


Monday = {  "Soup:":  x["Unnamed: 2"][FirstLane],
            "Snack:": x["Unnamed: 2"][FirstLane + 1],
            "Menu1:": x["Unnamed: 2"][FirstLane + 2],
            "Menu2:": x["Unnamed: 2"][FirstLane + 3],
            "Menu3:": x["Unnamed: 2"][FirstLane + 4]
}

Tuesday = { "Soup:":  x["Unnamed: 2"][FirstLane + DayDifference],
            "Snack:": x["Unnamed: 2"][FirstLane + DayDifference + 1],
            "Menu1:": x["Unnamed: 2"][FirstLane + DayDifference + 2],
            "Menu2:": x["Unnamed: 2"][FirstLane + DayDifference + 3],
            "Menu3:": x["Unnamed: 2"][FirstLane + DayDifference + 4]
}

Wednesday = { "Soup:":x["Unnamed: 2"][FirstLane + 2 * DayDifference],
              "Snack:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 1],
              "Menu1:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 2],
              "Menu2:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 3],
              "Menu3:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 4]
}

Thursday = { "Soup:": x["Unnamed: 2"][FirstLane + 3 * DayDifference],
             "Snack:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 1],
             "Menu1:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 2],
             "Menu2:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 3],
             "Menu3:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 4]
}

Friday = {  "Soup:":  x["Unnamed: 2"][FirstLane + 4 * DayDifference],
            "Snack:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 1],
            "Menu1:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 2],
            "Menu2:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 3],
            "Menu3:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 4]
}


week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = datetime.datetime.today().weekday()

WD = week[day]

WeekDay = globals()[WD]