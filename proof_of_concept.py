import requests
import json
from datetime import datetime
import threading

with open filename as f:
    content = f.readlines()

class travelThread(threading.Thread):
    def _init_(self,date,origin,destination):
        self.date = date
        self.origin = origin
        self.destination = destination

    def run():
        res = requests.get('https://www.oui.sncf/calendar/cdp/api/proposals/v3/outward/FRPAR/FRMZM/2019-09-20/12-HAPPY_CARD/2/fr/fr?extendedToLocality=true&onlyDirectTrains=true')
        jsoned_data = json.loads(res.content)

        for billet in jsoned_data:
            print(str(int(billet['totalPrice']) / 100) + '€ Départ : ' + str(billet['departureDate']).split('T')[1] + ' Arrivée : ' + str(billet['arrivalDate']).split('T')[1])
