def non_repeat_chars(s):

    for char in s:
        if s.count(char) == 1:
            return char
    else:
        return None
print(non_repeat_chars("aabbbvvccder"))