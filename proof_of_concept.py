import requests
import json
from datetime import datetime
import os
dirname = os.path.dirname(__file__)


def user_inputs_preprocessing(required_day, selected_departure_city,selected_arrival_city):

    with open(os.path.join(dirname, 'sncf_stations_codes.json'), 'r') as raw_stations_file:
        sncf_station_codes = json.load(raw_stations_file)

    departure_city_code = sncf_station_codes[selected_departure_city]
    arrival_city_code = sncf_station_codes[selected_arrival_city]

    return departure_city_code, arrival_city_code

def ping_sncf(departing_day, departure_city_code, arrival_city_code):

    options = '/12-HAPPY_CARD/2/fr/fr?extendedToLocality=true&onlyDirectTrains=true' # Don't care, don't touch
    url = 'https://www.oui.sncf/calendar/cdp/api/proposals/v3/outward'
    res = requests.get(url + '/FR' + departure_city + '/FR' + arrival_city + '/' + required_day + options)

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
    return useful_info


required_day = '2019-09-20' # Required format
selected_departure_city = 'Paris'
selected_arrival_city = 'Metz'
