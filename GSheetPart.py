import pandas as pd

sheet_code = "1kq9QMXmexts_Yqor7Jqhmo0IpU8BKZluSGWvrjNXcvU"
sheet_url = "https://docs.google.com/spreadsheets/d/"+sheet_code+"/export?format=csv"

x = pd.read_csv(sheet_url).to_dict()

print (x)
