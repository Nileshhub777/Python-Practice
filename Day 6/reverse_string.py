def words_reverse(text):
    reverse_str = ""
    for each in text.split():
        reverse_str = each + " " + reverse_str
    return reverse_str


print(words_reverse("sre is cool"))



