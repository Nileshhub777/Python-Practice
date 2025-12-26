def merge_dict(dict1,dict2):
    merged=dict1.copy()
    merged.update(dict2)
    return merged

print(merge_dict({'env':'prod'},{'region':'UK'}))

