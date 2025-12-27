def line_contain_errors():
    ctr=0
    with open('error.txt') as f:
        for line in f:
            if 'error' in line:
                ctr=ctr+1
    return ctr

print(line_contain_errors())
