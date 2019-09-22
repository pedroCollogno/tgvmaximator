import requests
import json
from datetime import datetime,date
import threading
import time
from proof_of_concept import apiCall
from checkNovelty import checkNovelty

""" content = []
filename = "travels.txt"
with open filename as f:
    content = f.readlines() """

required_day = '2019-09-28' # Required format
departure_city = 'PAR' # See other station's code
arrival_city = 'MZM'
content = [required_day+' '+departure_city+' '+arrival_city]
options = 'extendedToLocality=true&onlyDirectTrains=true' # Don't care, don't touch


class travelThread(threading.Thread):
    def __init__(self,date,origin,destination):
        threading.Thread.__init__(self)
        self.date = datetime.strptime(date,'%Y-%m-%d').date()
        self.origin = origin
        self.destination = destination
        self.id_list = []

    def run(self):
        while self.date>=date.today():
            print("Checking availibility for the trip from {0} to {1} on {2}".format(self.origin,self.destination, self.date.strftime("%Y-%m-%d")))
            info = apiCall(self.origin,self.destination,self.date)
            self.id_list = checkNovelty(self.id_list,info,self.origin,self.destination,self.date)
            time.sleep(60*10)

for travel in content:
    info = travel.split(' ')
    t = travelThread(info[0],info[1],info[2])
    t.start()
