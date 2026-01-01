def count_uppercase(text):
    upper_str = ""
    count = 0
    for ch in text:
        if ch.isupper():
            upper_str+=ch
            count += 1
    return upper_str, count


print(count_uppercase("DevOps is GREAT."))