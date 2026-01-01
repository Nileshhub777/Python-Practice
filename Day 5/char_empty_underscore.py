def replace_space_underscore(text):
    new_str=""
    for ch in text:
        if ch == " ":
            new_str+="_"
        else:
            new_str=new_str+ch
    return new_str
print(replace_space_underscore("Devops is the trend boss"))