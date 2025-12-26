def check_list_values(list,value):
    if value in list:
        return True
    else:
        return False

print(check_list_values([1,2,3,4,5,6], 2))