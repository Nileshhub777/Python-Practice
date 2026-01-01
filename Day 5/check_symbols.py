def check_symbols(text):
    new_str=''
    for ch in text:
        if not ch.isalnum() and ch != ' ':
            new_str+=ch
    return new_str

print(check_symbols("dev#$%^&hh$iitufh"))
