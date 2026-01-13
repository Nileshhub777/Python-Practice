def count_sub_str(string, sub_str):
    count=0
    for i in range(len(string)):
        if string.startswith(sub_str,i):
            count+=1
    return count

print(count_sub_str("abcd", 'abc'))
