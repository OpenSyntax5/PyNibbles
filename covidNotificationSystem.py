import datetime
import time
import requests
from plyer import notification

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/USA/")
except:
    print("There was an error. Please check your Internet connection.")

if (covidData != None):
    data = covidData.json()['Success']

    while(True):
        notification.notify(
            title = "COVID-19 Statistics on {}".format(datetime.date.today()),
            message = "Total cases : {totalcases}\nCases today : {todaycases}\nDeaths Today : {todaydeaths}\nTotal active : {active}".format(
                totalcases = data['cases'],
                todaycases = data['todayCases'],
                todaydeaths = data['todayDeaths'],
                active = data['active']),
            timeout = 20
        )
        time.sleep(60*60*4)
