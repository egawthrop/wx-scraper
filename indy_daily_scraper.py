import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path


# get today's date
today = datetime.now()

# get yesterday's date
yesterday = datetime.now() - timedelta(1)
print("Yesterday's date:", yesterday)

# extract month day and year as strings so that leading zeros are retained
today_month = today.strftime('%m')
today_day = today.strftime('%d')
today_year = today.strftime('%Y')

data_month = yesterday.strftime('%m')
data_day = yesterday.strftime('%d')
data_year = yesterday.strftime('%Y')

# define station ID
station = 'KININDIA550'

# define and get URL, parse text and extract daily rainfall 
wx_url = f'https://www.wunderground.com/dashboard/pws/{station}/graph/{data_year}-{data_month}-{data_day}/{data_year}-{data_month}-{data_day}/daily'
wx = requests.get(wx_url)
doc = BeautifulSoup(wx.text, 'html.parser')
precip_section = doc.find('span', class_='test-false wu-unit wu-unit-rain').parent
rain_value = float(precip_section.find('span', class_='wu-value wu-value-to').text)
#rain_list = doc.findAll('span', class_ = "wu-value wu-value-to")
data_date = f'{data_month}:{data_day}:{data_year}'
today_date = f'{today_month}:{today_day}:{today_year}'

# check to see if csv already exists, and if not create a new one 
path_to_file = 'daily2.csv'
the_path = Path(path_to_file)

if the_path.is_file():
    print(f'The file {path_to_file} exists')
else:
    column_names = ["Station", "Date", "Rainfall"]
    df = pd.DataFrame(columns = column_names)
    df.to_csv('daily2.csv', index = False)

# open csv, add new data 
df = pd.read_csv('daily2.csv')
df2 = {'Station': station, 'Today Date': today_date, 'Data Date': data_date, 'Rainfall': rain_value}
#df = df.append(df2, ignore_index = True)
df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)

# write new csv 
df.to_csv('daily2.csv', index = False)
