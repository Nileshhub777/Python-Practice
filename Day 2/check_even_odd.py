def check_even_odd_ctr(list):
    even_ctr=0
    odd_ctr=0

    for each in list:
        if each%2==0:
            even_ctr=even_ctr+1
        else:
            odd_ctr=odd_ctr+1
    print(even_ctr,  odd_ctr)
print(check_even_odd_ctr([2,4,6,2,3,7,9]))