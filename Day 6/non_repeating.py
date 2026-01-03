def non_repeating_char(text):
    count_c = {}
    for ch in text:
        if ch in count_c:
            count_c[ch]+=1
        else:
            count_c[ch]=1

    for ch in text:
        if count_c[ch] == 1:
            return ch
print(non_repeating_char("swisss"))


