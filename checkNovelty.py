import json

def checkNovelty(dic_list,date,origin):
    new_ids = []
    old_ids = []
    with open id+'.json' as json_file:
        old_dic_list = json.load(json_file)
    for dic in dic_list:
        new_ids.append(dic.id)
    for old_dic in old_dic_list:
        old_ids.append(old_dic.id)

    new_ids.sort()
    old_ids.sort()

    if new_ids != old_ids:
        notifyUser()

        with open id+'.json' as new_json:
            json.dump(dic_list,new_json)
