def check_str_palin(text):
    if text.lower() == text.lower()[::-1]:
        return True
    else:
        return False

print(check_str_palin("madam"))