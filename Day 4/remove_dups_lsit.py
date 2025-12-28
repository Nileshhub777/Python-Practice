def remove_dups_list(lst):
    uniq_lst=[]
    for each in lst:
        if each not in uniq_lst:
            uniq_lst.append(each)
    return uniq_lst

print(remove_dups_list([1,2,2,2,3,3,4,4,5]))


# “I iterate through the list and add elements to a new list only if they’re not already present, which removes duplicates while preserving order.”