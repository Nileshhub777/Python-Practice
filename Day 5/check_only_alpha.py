def check_alphanumeric(text):
    for ch in text:
        if not ch.isalpha():
            return False
    return True

print(check_alphanumeric("Devops123"))
