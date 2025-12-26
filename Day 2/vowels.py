def vowels_string(str1):
    new_modified_str = ''
    count=0
    for each in str1:
        if each in 'aeiou':
            new_modified_str=new_modified_str + each
            count=count+1
    return new_modified_str,count

print(vowels_string("hello"))




# “I loop through the string and increment a counter whenever I encounter a vowel.”