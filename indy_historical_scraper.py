import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


yesterday = datetime.now() - timedelta(1)
print("Yesterday's date:", yesterday)

month = yesterday.strftime('%m')
day = yesterday.strftime('%d')
year = yesterday.strftime('%Y')
month 
day 
year

wx_url = f'https://www.wunderground.com/dashboard/pws/KININDIA334/graph/{year}-{month}-{day}/{year}-{month}-{day}/daily'

wx = requests.get(wx_url)
doc = BeautifulSoup(wx.text, 'html.parser')
rain_list = doc.findAll('span', class_='test-false wu-unit wu-unit-rain ng-star-inserted')
date = f'{month}:{day}:{year}'
value = rain_list[2].text[:-4]

rainfall

month = ["07"]
day = [*range(20, 24, 1)]
daily_rainfall = []
for mmonth in month:
    for dday in day:
        repeat = False
        wx_url = f'https://www.wunderground.com/dashboard/pws/KINNOBLE123/graph/2021-{mmonth}-{dday}/2021-{mmonth}-{dday}/daily'
        wx = requests.get(wx_url)
        doc = BeautifulSoup(wx.text, 'html.parser')
        rain_list = doc.findAll('span', class_='test-false wu-unit wu-unit-rain ng-star-inserted')
        rainfall = {
                'date': f'{mmonth}:{dday}:2021',
                'value': rain_list[2].text.strip()
                }
        #for (index, rain) in enumerate(rain_list):
        # Create a new dictionary to populate with formatted date
        # index being the column that corresponds to the order of dates in the date_list above
            #if index == 2:
             #   rainfall = {
             #   'date': f'{mmonth}:{dday}:2021',
             #   'value': rain.text.strip()
              #  }
        print(rainfall)
        daily_rainfall.append(rainfall)
        today_url = wx.url
        next_url = f'https://www.wunderground.com/dashboard/pws/KINNOBLE123/graph/2021-{mmonth}-{dday+1}/2021-{mmonth}-{dday+1}/daily'
        tomorrow_wx = requests.get(next_url)
        tomorrow_url = tomorrow_wx.url
        if today_url == tomorrow_url:
            print('repeat date, try next month')
            repeat = True
            break
    else: 
        continue
    if repeat:
        break

for x in xrange(10):
    for y in xrange(10):
        print x*y
        if x*y > 50:
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break
    
        


for word1 in buf1: 
    find = False 
    for word2 in buf2: 
        ... 
        if res == res1: 
            print "BINGO " + word1 + ":" + word2 
            find = True 
            break             # <-- break here too
    if find: 
        break 

daily_rainfall_df = pd.DataFrame(daily_rainfall)

# remove dates past jly 13 for now 
daily_rainfall_df = daily_rainfall_df.iloc[:-18 , :]


daily_rainfall_df[['rainfall', 'units']] = daily_rainfall_df['value'].str.split(r"\s", expand=True)

   

daily_rainfall_df['rainfall'] = daily_rainfall_df['rainfall'].astype(float)

daily_rainfall_df = daily_rainfall_df.drop(columns=['value'])  

daily_rainfall_df['rainfall'].sum()



        #for item,  in rain:
         #   precip = rain.text.strip()
       # daily_rainfall.append(precip)
