def remove_duplicates(inp):
    new_list=[]
    for char in inp:
        if char not in new_list:
            new_list.append(char)
    return new_list
print(remove_duplicates([1,2,2,3,3,3,4]))