import requests
import json
from datetime import datetime,date
import threading
import time
from proof_of_concept import api_call
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
        self.iteration_counter = 0

    def run(self):
        while self.date >= date.today():
            print("{0} : Checking availibility for the trip from {1} to {2} on {3}".format(datetime.now().strftime('%H:%M:%S'),self.origin, self.destination, self.date.strftime("%Y-%m-%d")))
            info = api_call(self.origin, self.destination, self.date.strftime("%Y-%m-%d"))
            self.id_list = check_novelty(self.id_list, info, self.origin, self.destination, self.date, self.user_list, self.iteration_counter)
            self.iteration_counter += 1
            time.sleep(60 * 10)

for travel in content:
    info = travel.split(' ')
    names = []
    for name in info[3:]:
        names.append(name)
    info = info[:2]
    info.append(names)
    print(info)
    t = TravelThread(info[0], info[1], info[2], info[3])
    t.start()
