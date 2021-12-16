import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path

# get yesterday's date
yesterday = datetime.now() - timedelta(1)
print("Yesterday's date:", yesterday)

# extract month day and year as strings so that leading zeros are retained
month = yesterday.strftime('%m')
day = yesterday.strftime('%d')
year = yesterday.strftime('%Y')

# define station ID
station = 'KININDIA334'

# define and get URL, parse text and extract daily rainfall 
wx_url = f'https://www.wunderground.com/dashboard/pws/{station}/graph/{year}-{month}-{day}/{year}-{month}-{day}/daily'
wx = requests.get(wx_url)
doc = BeautifulSoup(wx.text, 'html.parser')
rain_list = doc.findAll('span', class_='test-false wu-unit wu-unit-rain ng-star-inserted')
date = f'{month}:{day}:{year}'
value = rain_list[2].text[:-4]

# check to see if csv already exists, and if not create a new one 
path_to_file = 'daily.csv'
the_path = Path(path_to_file)

if the_path.is_file():
    print(f'The file {path_to_file} exists')
else:
    column_names = ["Station", "Date", "Rainfall"]
    df = pd.DataFrame(columns = column_names)
    df.to_csv('daily.csv', index = False)

# open csv, add new data 
df = pd.read_csv('daily.csv')
df2 = {'Station': station, 'Date': date, 'Rainfall': value}
df = df.append(df2, ignore_index = True)

# write new csv 
df.to_csv('daily.csv', index = False)