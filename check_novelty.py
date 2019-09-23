import json
from notify_user import notify_user

def check_novelty(old_ids, dic_list, origin, destination, date, user_list):
    new_ids = []
    for dic in dic_list:
        if dic['is_tgvmax']:
            if not dic['id'] in old_ids:
                print("New train detected, Départ : " + dic['departure_time'].strftime("%Hh%M"))
                notify_user(origin, destination, date, dic, user_list)
        new_ids.append(dic['id'])
    return new_ids
            
