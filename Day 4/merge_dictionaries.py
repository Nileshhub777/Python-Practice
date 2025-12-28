def merge_dictionaries(dict1, dict2):
    new_dict={}
    for key, value in dict1.items():
        new_dict[key]=value
    for key, value in dict2.items():
        new_dict[key]=value

    return new_dict

print(merge_dictionaries({'env':'uat'},{'region':'India'}))


