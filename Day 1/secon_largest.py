def check_second_largest(lst):
    lst.sort()
    return lst[-2]

print(check_second_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))