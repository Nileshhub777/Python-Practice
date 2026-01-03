def remove_dups_words(text):
    new_str = ""
    for word in text.split():
        if word not in new_str.split():
            new_str = new_str + " " + word
    return new_str.strip()

print(remove_dups_words("python is python and devops is devops"))