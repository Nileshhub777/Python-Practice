def sort_dic_values(dic1):
    new_dict={}
    values=(list(dic1.values()))
    values.sort()
    print(values)

    for value in values:
        for key in dic1:
            if dic1[key] == value and key not in new_dict:
                new_dict[key]=value
                break
    return new_dict

print(sort_dic_values ({'a': 3, 'b': 1, 'c': 2}))








