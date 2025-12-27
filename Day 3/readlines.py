def read_count_lines():
    ctr=0
    with open('abc.txt') as f:
        for each in f:
            ctr+=1
    return ctr

print(read_count_lines())