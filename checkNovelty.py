import json
from notifyUser import notifyUser

def checkNovelty(old_ids,dic_list,origin,destination,date):
    new_ids = []
    for dic in dic_list:
        if dic['is_tgvmax']:
            if not dic['id'] in old_ids:
                print("New train detected, Départ : " + dic['departure_time'].strftime("%Hh%M"))
                notifyUser(origin,destination,date,dic)
        new_ids.append(dic['id'])
    return new_ids
            
