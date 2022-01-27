import pandas
import Codes
import datetime

sheet_url = "https://docs.google.com/spreadsheets/d/"+Codes.GSheet+"/export?format=csv"

x = pandas.read_csv(sheet_url).to_dict()

FirstLane = 4
DayDifference = 7

Monday = {  "Polévka:":  x["Unnamed: 2"][FirstLane],
            "Ňamka:": x["Unnamed: 2"][FirstLane + 1],
            "Oběd 1:": x["Unnamed: 2"][FirstLane + 2],
            "Oběd 2:": x["Unnamed: 2"][FirstLane + 3],
            "Oběd 3:": x["Unnamed: 2"][FirstLane + 4]
}

Tuesday = { "Polévka:":  x["Unnamed: 2"][FirstLane + DayDifference],
            "Ňamka:": x["Unnamed: 2"][FirstLane + DayDifference + 1],
            "Oběd 1:": x["Unnamed: 2"][FirstLane + DayDifference + 2],
            "Oběd 2:": x["Unnamed: 2"][FirstLane + DayDifference + 3],
            "Oběd 3:": x["Unnamed: 2"][FirstLane + DayDifference + 4]
}

Wednesday = { "Polévka:":x["Unnamed: 2"][FirstLane + 2 * DayDifference],
              "Ňamka:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 1],
              "Oběd 1:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 2],
              "Oběd 2:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 3],
              "Oběd 3:": x["Unnamed: 2"][FirstLane + 2 * DayDifference + 4]
}

Thursday = { "Polévka:": x["Unnamed: 2"][FirstLane + 3 * DayDifference],
             "Ňamka:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 1],
             "Oběd 1:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 2],
             "Oběd 2:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 3],
             "Oběd 3:": x["Unnamed: 2"][FirstLane + 3 * DayDifference + 4]
}

Friday = {  "Polévka:":  x["Unnamed: 2"][FirstLane + 4 * DayDifference],
            "Ňamka:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 1],
            "Oběd 1:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 2],
            "Oběd 2:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 3],
            "Oběd 3:": x["Unnamed: 2"][FirstLane + 4 * DayDifference + 4]
}

def ChooseDay():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = datetime.datetime.today().weekday()
    WD = week[day]
    return globals()[WD]