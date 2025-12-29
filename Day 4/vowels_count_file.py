def count_vowels_file():
    ctr = 0
    with open('abc.txt', 'r') as f:
        for line in f:
            for ch in line:
                if ch in 'aeiouAEIOU':
                    ctr += 1
    return ctr
print(count_vowels_file())