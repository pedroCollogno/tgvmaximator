import requests
import json
from datetime import datetime

required_day = '2019-09-20' # Required format
departure_city = 'PAR' # See other station's code
arrival_city = 'MZM'

options = 'extendedToLocality=true&onlyDirectTrains=true' # Don't care, don't touch
res = requests.get('https://www.oui.sncf/calendar/cdp/api/proposals/v3/outward/FR' + departure_city +'/FR' + arrival_city + '/' + required_day + '/12-HAPPY_CARD/2/fr/fr?' + options)

jsoned_data = json.loads(res.content)

for billet in jsoned_data:

    # Useful infos : billet['totalPrice'] (in centimes), billet['departureDate'] and billet['arrivalDate'] (only care about the time, discard the rest)
    departure_time = datetime.strptime(str(billet['departureDate']), "%Y-%m-%dT%H:%M")
    arrival_time = datetime.strptime(str(billet['arrivalDate']), "%Y-%m-%dT%H:%M")

    print(str(int(billet['totalPrice']) / 100) + '€ Départ : ' + departure_time.strftime("%Hh%M") + ' Arrivée : ' + arrival_time.strftime("%Hh%M"))