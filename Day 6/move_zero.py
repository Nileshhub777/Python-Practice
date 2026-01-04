def move_all_zeros(lst):
    result=[]
    zero_ctr=0

    for num in lst:
        if num == 0:
            zero_ctr+=1
        else:
            result.append(num)

    for i in range(zero_ctr):
        result.append(0)

    return result

print(move_all_zeros([1,2,4,3,0,3,40,1,0,2,3,0,9]))
