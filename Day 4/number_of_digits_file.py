def number_of_digits():
    with open('abc.txt') as f:
        ctr =0
        for line in f:
            for ch in line:
                if ch.isdigit():
                    ctr += 1
    return ctr

print(number_of_digits())