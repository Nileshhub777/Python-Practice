def unique_check(text):
    unique_list = ""
    for each in text:
        if each in unique_list:
            return False
        unique_list += each
    return unique_list

print(unique_check('devops'))