def count_chars_file():
    with open('abc.txt', 'r') as f:
        ctr = 0
        for line in f:
            for char in line:
                if char != '\n':
                    ctr+=1
    return ctr

print(count_chars_file())