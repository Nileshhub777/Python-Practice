def common_elements(list1,list2):
    common_list=[]
    for element in list1:
        if element in list2 and element not in common_list:
            common_list.append(element)
    return common_list
print(common_elements([1,2,3,4,5],[1,26,7,8,3,4]))


# “I iterate through the first list and check if elements exist in the second list, storing common values in a new list.”