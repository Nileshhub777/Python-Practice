def two_common_dict(dict1,dict2):
    dict3=[]
    for k in dict1:
        if k in dict2:
            dict3.append(k)

    return dict3

print(two_common_dict({'env': 'prod', 'region': 'eu'},{'env': 'uat', 'team': 'sre'}))