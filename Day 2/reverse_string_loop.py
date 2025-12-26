def reverse_string(str1):
    rev_str= ''

    for i in str1:
        rev_str = i + rev_str
        #print(rev_str)
    return rev_str

print(reverse_string("hello"))
