from re import escape
import pandas as pd
import requests
from bs4 import BeautifulSoup


month = ["06"]
day = [*range(1, 32, 1)]
daily_rainfall = []
for mmonth in month:
    for dday in day[0:1]: 
        future = False
        wx_url = f'https://www.wunderground.com/dashboard/pws/KINNOBLE123/graph/2021-{mmonth}-{dday}/2021-{mmonth}-{dday}/daily'
        wx = requests.get(wx_url)
        #if rainfall['date'] == f'{mmonth}:{dday}:2021':
        #    future = True
        #    break
        doc = BeautifulSoup(wx.text, 'html.parser')
        rain_list = doc.findAll('span', class_='test-false wu-unit wu-unit-rain ng-star-inserted')
        for (index, rain) in enumerate(rain_list):
            # Create a new dictionary to populate with formatted date
            # index being the column that corresponds to the order of dates in the date_list above
            if index == 2:
                rainfall = {
                'date': f'{mmonth}:{dday}:2021',
                'value': rain.text.strip()
                }
        print(rainfall)
        daily_rainfall.append(rainfall)
    for dday in day[1:]: 
        future = False
        wx_url = f'https://www.wunderground.com/dashboard/pws/KINNOBLE123/graph/2021-{mmonth}-{dday}/2021-{mmonth}-{dday}/daily'
        wx = requests.get(wx_url)
        if rainfall['date'] == f'{mmonth}:{dday}:2021':
            future = True
            break
        doc = BeautifulSoup(wx.text, 'html.parser')
        rain_list = doc.findAll('span', class_='test-false wu-unit wu-unit-rain ng-star-inserted')
        for (index, rain) in enumerate(rain_list):
            # Create a new dictionary to populate with formatted date
            # index being the column that corresponds to the order of dates in the date_list above
            if index == 2:
                rainfall = {
                'date': f'{mmonth}:{dday}:2021',
                'value': rain.text.strip()
                }
        print(rainfall)
        daily_rainfall.append(rainfall)
    if future:
        break 
        


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
