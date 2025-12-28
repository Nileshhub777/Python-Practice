def element_max_no_element(lst):
    dict1={}
    for each in lst:
        if each in dict1:
            dict1[each]=dict1[each]+1
        else:
            dict1[each]=1
    print(dict1)

    max_count=0
    max_element=None

    for key in dict1:
        if dict1[key] > max_count:
            max_count=dict1[key]
            max_element=key
    return max_element,max_count

print(element_max_no_element([1,2,2,2,3,3,4,3,5]))



# “I count occurrences using a dictionary, then iterate through it to find the element with the highest frequency and return both the element and its count.”