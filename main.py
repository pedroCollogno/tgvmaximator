import requests
import json
from datetime import datetime,date
import threading
from crontab import CronTab
from proof_of_concepts import lafonction

content = []
filename = "travels.txt"
with open filename as f:
    content = f.readlines()

required_day = '2019-09-20' # Required format
departure_city = 'PAR' # See other station's code
arrival_city = 'MZM'

options = 'extendedToLocality=true&onlyDirectTrains=true' # Don't care, don't touch


class travelThread(threading.Thread):
    def _init_(self,date,origin,destination,option):
        self.date = datetime.strptime(date,%Y-%m-%d)
        self.origin = origin
        self.destination = destination

    def run():
        while self.date<date.today:
            lafonction(self.date,self.origin,self.destination)
            time.sleep(60*10)

for travel in content:
    info = travel.split(' ')
    t = travelThread(info[0],info[1],info[2],option)
    t.start()
