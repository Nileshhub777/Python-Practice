def count_digits_string(text):
    new_str = ""
    for ch in text:
        if ch in "0123456789":
            new_str=new_str+ch
    return len(new_str)

print(count_digits_string("dev123ops998"))
