def count_digits_str(text):
    ctr = 0
    for ch in text:
        if ch.isdigit():
            ctr = ctr + 1
    return ctr


print(count_digits_str('Devops1234567'))


