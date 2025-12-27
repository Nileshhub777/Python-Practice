def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)

    return merged_dict

print(merge_dictionaries({'env':'prod'}, {'region':'LA'}))