def check_list_sorted_YN(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

print(check_list_sorted_YN([1,2,4,3,5]))


# I loop through the list and compare each element with the next one.
# If any element is greater than the next, I return False.
# If the loop completes, the list is sorted.”