from forecastiopy import *
import csv
import os
import pandas as pd
import datetime 
import time

apikey = 'your_apikey'
 
Boulder = [40.014984, -105.270546, 1451631600]
Boulder_Time = 1451631600
 
fio = ForecastIO.ForecastIO(apikey,
                            latitude=Boulder[0],
                            longitude=Boulder[1],
                            time=str(Boulder[2])) 
print 'Latitude', fio.latitude, 'Longitude', fio.longitude
print 'Timezone', fio.timezone
print fio.get_url() # You might want to see the request url
print

req_list = {}
b_mth = '12/'
for b_day in range(1,32):
    dt = datetime.datetime(2017, 12, b_day, 0, 0)
    req_list[b_mth + str(b_day) + '/2017'] = int((time.mktime(dt.timetuple())))

sortedReqList = sorted(req_list.items())

    
columns = ['Date', 'cloudCover', 'apparentTemperatureMax', 'apparentTemperatureMin', 'temperatureMax', 'temperatureMin', 'windSpeed', 'humidity', 'visibility', 'time']
index = ['Row']
dF = pd.DataFrame(columns = columns, index = index)
dF1= pd.DataFrame(columns = columns, index = index)
csv_file = "C:\Temp\Boulder_Dec_2017_Daily_Weather_Forecast.csv"

for req_day in sortedReqList:
    Boulder_Time = req_day[1]
    fio = ForecastIO.ForecastIO(apikey,
                            latitude=Boulder[0],
                            longitude=Boulder[1],
                            time=str(Boulder_Time))

    if fio.has_daily() is True:
        daily = FIODaily.FIODaily(fio)
        for day in xrange(0, daily.days()):
            for item in daily.get_day(day).keys():
                print item + ' : ' + unicode(daily.get_day(day)[item])
                dF['Date'] = req_day[0]
                if item == 'time':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'cloudCover':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'apparentTemperatureMax':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'apparentTemperatureMin':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'temperatureMax':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'temperatureMin':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'windSpeed':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'humidity':
                    dF[str(item)] = daily.get_day(day)[item]
                if item == 'visibility':
                    dF[str(item)] = daily.get_day(day)[item]
            dF1 = dF1.append(dF)    
    else:
        print 'No Daily data'


dF1.to_csv(csv_file, sep=',')

new_dF = pd.read_csv(csv_file,index_col=0)
print new_dF
