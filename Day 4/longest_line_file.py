def longest_line_file():
    longest = ''
    with open('abc.txt') as f:
        for line in f:
            if len(line) > len(longest):
                longest = line
    return line
print(longest_line_file())