def average_nums(avg_list):
    total =0
    for n in avg_list:
        total+=n
    return total/len(avg_list)

print(average_nums([1,2,3,4,5,6,7]))


#built-in

def average_nums2(avg_list):
    return sum(avg_list)/len(avg_list)

print(average_nums2([1,2,3,4,5,8,7]))