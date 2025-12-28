def reverse_dict_items(dict1):
    new_dict = {}
    for key, value in dict1.items():
        new_dict[value] = key
    return new_dict

print(reverse_dict_items({'a':1,'b':2,'c':3}))


# “I iterate through dictionary items and swap keys and values into a new dictionary.”