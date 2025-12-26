def sum_list_nums(numlist):
    return sum(numlist)

print(sum_list_nums([1,2,3,4,5]))


def sum_list_nums2(numlist):
    total =0
    for each in numlist:
        total=total + each
    return total

print(sum_list_nums2([1,2,3,44,55]))