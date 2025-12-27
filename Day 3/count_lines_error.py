def count_lines_error():
    ctr=0
    with open('error.txt', 'r') as f:
        for each in f:
            if 'error' in each.lower():
                ctr+=1
    return ctr
print(count_lines_error())