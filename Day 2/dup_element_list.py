def duplicate_element_list(list):
    output=[]
    for element in list:
        if element not in output:
            output.append(element)
    return output

print(duplicate_element_list([1,22,2,33,33,22,2,3,3,4,5]))


# “I iterate through the list and store only first occurrences in a new list, which removes duplicates while preserving order.”