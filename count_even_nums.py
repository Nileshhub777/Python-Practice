def count_even_nums(numlist):
    count = 0
    for num in numlist:
        if num % 2 == 0:
            count+=1
    return count

print(count_even_nums([1,2,3,4,5,6,7,8,10,12,14,16,18]))