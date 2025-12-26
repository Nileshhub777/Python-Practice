def check_char_count(a,b):
     return a.count(b)

print(check_char_count('banana', 'a'))


def check_char2_count(x,y):
    count=0
    for ch in x:
        if ch == y:
            count=count+1
    return count

print(check_char2_count('banana', 'a'))