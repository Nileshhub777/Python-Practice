def check_even_odd_ctr(list):
    even_ctr=0
    odd_ctr=0

    for each in list:
        if each%2==0:
            even_ctr=even_ctr+1
        else:
            odd_ctr=odd_ctr+1
    return even_ctr,odd_ctr

even,odd=check_even_odd_ctr([1,2,3,4,5,6,7,8,9])




print('even:',even)
print('odd:',odd)



# I loop through the list and use modulo to check if a number is even or odd.
# I increment separate counters and return them.”