def reverse_each_word(text):
    new_str=""
    for each in text.split():
        temp=""
        for ch in each:
            temp=ch+temp
        new_str+=temp + " "
    return new_str.strip()

print(reverse_each_word("sre is top level"))




// “I reverse each word using a temp variable and append it to result”