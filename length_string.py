def length_string(string):
    len_ctr=0
    for ch in string:
        len_ctr=len_ctr+1
    return len_ctr
print(length_string(input("Enter a string: ")))