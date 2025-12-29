def remove_none_dict(dict1):
    dict_new={}
    for key, value in dict1.items():
        if dict1[key] != None:
            dict_new[key] = value
    return dict_new

print(remove_none_dict({'env': 'prod', 'region': None, 'team': 'sre'}))