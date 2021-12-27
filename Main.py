import pandas as pd
sheet_code = "1kq9QMXmexts_Yqor7Jqhmo0IpU8BKZluSGWvrjNXcvU"
sheet_url = "https://docs.google.com/spreadsheets/d/"+sheet_code+"/export?format=csv"

x = pd.read_csv(sheet_url).to_dict()

class ScholarestMenu:
    def __init__(self, Soup, Menu1, Menu2, Menu3):
        self.Soup = Soup
        self.Menu1 = Menu1
        self.Menu2 = Menu2
        self.Menu3 = Menu3

#Variables
RowDifferences = 7
MenuRow = 0
######



Monday = ScholarestMenu(x["Unnamed: 1"][MenuRow], x["Unnamed: 1"][MenuRow + 2], x["Unnamed: 1"][MenuRow + 3], x["Unnamed: 1"][MenuRow + 4])

print(Monday.Soup)
print(Monday.Menu1)
print(Monday.Menu2)
print(Monday.Menu3)