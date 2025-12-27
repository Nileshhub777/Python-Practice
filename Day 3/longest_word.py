def longest_word():
    with open('abc.txt') as f:
        longest=''
        for line in f:
            for word in line.split():
                if len(word) > len(longest):
                    longest = word
    return longest

print(longest_word())