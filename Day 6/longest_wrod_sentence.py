def longest_word(text):
    longest=""
    for word in text.split():
        if len(word) > len(longest):
            longest=word
    return longest

print(longest_word("python is amazing devops skill"))
