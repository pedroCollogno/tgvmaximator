import requests
import json
from datetime import datetime,date
import threading
import time
from proof_of_concept import api_call, SncfVoyage
from check_novelty import check_novelty

content = []
filename = "travels.txt"
with open(filename) as f:
    content = f.read().splitlines()

class TravelThread(threading.Thread):
    def __init__(self, date, origin, destination, user_list):
        threading.Thread.__init__(self)
        self.date = datetime.strptime(date,'%Y-%m-%d').date()
        self.origin = origin
        self.destination = destination
        self.id_list = []
        self.user_list = user_list

    def run(self):
        while self.date >= date.today():
            print("Checking availibility for the trip from {0} to {1} on {2}".format(self.origin, self.destination, self.date.strftime("%Y-%m-%d")))
            sncf_voyage = SncfVoyage(self.origin, self.destination, self.date.strftime("%Y-%m-%d"))
            info = sncf_voyage.api_call()
            self.id_list = check_novelty(self.id_list, info, self.origin, self.destination, self.date, self.user_list)
            time.sleep(60 * 10)

for travel in content:
    info = travel.split(' ')
    print(info)
    t = TravelThread(info[0], info[1], info[2], ['Marin','Renaud','Erwan','Pedro'])
    t.start()
