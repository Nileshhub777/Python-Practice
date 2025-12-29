def compare_dictinaries(dict1, dict2):

    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] != dict2[key]:
            return False
    return True

print(compare_dictinaries({'a':1, 'b':2},{'b':2, 'a':1}))