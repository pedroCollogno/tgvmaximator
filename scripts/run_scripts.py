import requests
import json
from datetime import datetime,date
import time
from proof_of_concept import api_call
from check_novelty import check_novelty

content = []
filename = "travels.txt"
with open(filename) as f:
    content = f.read().splitlines()

for travel in content:
    info = travel.split(' ')
    print(info)
    date = datetime.strptime(info[0],'%Y-%m-%d').date()
    origin = info[1]
    destination = info[2]
    id_list = []
    user_list = ['Pedro']
    print("Checking availibility for the trip from {0} to {1} on {2}".format(origin, destination, date.strftime("%Y-%m-%d")))
    info = api_call(origin, destination, date.strftime("%Y-%m-%d"))
    id_list = check_novelty(id_list, info, origin, destination, date, user_list)