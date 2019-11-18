import requests
import json
PAGE_ACCESS_TOKEN = 'EAADvFZA80kBIBAHmq7D3yk3RV9hTfnh90Yo1w2ZB1pZCyqEPjB6PbhOZA1USIYS94cC4ZBpFkRmOUv1maVkyidZB6j3hK9nyHrZABEdkZBS1ynwKU7CrQCZB6EXC7kZAJYRMeUSp3kZCIsqfeMeGfAvf8qGV6cJjQzoShUAoZC3S6domtQZDZD'

def notify_user_messenger(origin, destination, date, dic, user_list):
    for user in user_list:
        with open('emails_to_ping.json') as json_file:
            user_info = json.load(json_file)
            sender_psid = user_info[user]['psid']
            name = user_info[user]['name']
            text = """\
                Bonjour M. {0},
                Un nouveau train TGVMax est disponible pour votre trajet de {1} a {2} le {3}. Il part à {4}. 
                Si cet horaire vous correspond vous pouvez aller manger nos couilles en salade.
                
                Cordialement,
                L'équipe TGVMaximator""".format(name, origin, destination, date.strftime("%Y-%m-%d"), dic['departure_time'].strftime("%Hh%M"))

            request_body = {
                'messaging_type': 'RESPONSE',
                'recipient': {
                'id': sender_psid,
                },
                'message': {
                'text': text,
                },
            }
            # Send the HTTP request to the Messenger Platform
            r = requests.post("https://graph.facebook.com/v2.6/me/messages", json=request_body, params={'access_token': PAGE_ACCESS_TOKEN})
            if(r.status_code == 200):
                print("Message sent to {}".format(name))
            else:
                print("Error sending message to {}".format(name))
            