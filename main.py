import requests
import json
from datetime import datetime,date
import threading
import time
from proof_of_concept import api_call
from check_novelty import check_novelty



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
            
while True:
    content = []
    filename = "travels.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    for travel in content:
        if(len(travel.strip()) > 0):
            info = travel.split(' ')
            date = info[0]
            origin = info[1]
            destination = info[2]
            names = []
            for name in info[3:]:
                names.append(name)
            print(info)
            print("{0} : Checking availibility for the trip from {1} to {2} on {3}".format(datetime.now().strftime('%H:%M:%S'),origin, destination, date.strftime("%Y-%m-%d")))
            travel_data = api_call(origin, destination, date.strftime("%Y-%m-%d"))
            id_list = check_novelty(id_list, travel_data, origin, destination, date, user_list, iteration_counter)
            iteration_counter += 1
            time.sleep(60 * 10)
