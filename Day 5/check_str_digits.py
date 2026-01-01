def check_only_digits(text):
    for ch in text:
        if not ch.isdigit():
            return False
    return True
print(check_only_digits("123"))