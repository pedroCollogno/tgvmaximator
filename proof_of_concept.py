import requests
import json
from datetime import datetime

required_day = '2019-09-20' # Required format
departure_city = 'PAR' # See other station's code
arrival_city = 'MZM'

options = 'extendedToLocality=true&onlyDirectTrains=true' # Don't care, don't touch
res = requests.get('https://www.oui.sncf/calendar/cdp/api/proposals/v3/outward/FR' + departure_city +'/FR' + arrival_city + '/' + required_day + '/12-HAPPY_CARD/2/fr/fr?' + options)

jsoned_data = json.loads(res.content)

useful_info = []
for billet in jsoned_data:

    # Useful infos : billet['totalPrice'] (in centimes), billet['departureDate'] and billet['arrivalDate'] (only care about the time, discard the rest)
    billet_info = {'departure_time': datetime.min, 'arrival_time': datetime.max, 'price': 10000000000000000, 'is_tgvmax': False, 'is_trakos': True}

    departure_time = datetime.strptime(str(billet['departureDate']), "%Y-%m-%dT%H:%M")
    arrival_time = datetime.strptime(str(billet['arrivalDate']), "%Y-%m-%dT%H:%M")

    billet_info['price'] = int(billet['totalPrice'])
    billet_info['departure_time'] = departure_time
    billet_info['arrival_time'] = arrival_time
    billet_info['is_tgvmax'] = (billet_info['price'] == 0)
    # A 'gros trakos' is defined as a way too early or way too late departure time
    billet_info['is_trakos'] = (7 > billet_info['departure_time'].hour or billet_info['departure_time'].hour > 22)

    print(str(billet_info['price'] / 100) + '€ Départ : ' + billet_info['departure_time'].strftime("%Hh%M") + ' Arrivée : ' + billet_info['arrival_time'].strftime("%Hh%M"))
    print('TGVMax ? ' + str(billet_info['is_tgvmax']) + ' Un gros trakos ? ' + str(billet_info['is_trakos']))

    useful_info.append(billet_info)
