def shortest_word_sentence(text):
    words = text.split()
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

print(shortest_word_sentence("python is amazing"))



# “I split the sentence into words, assume the first word is the shortest, then compare each word and update if a shorter one is found.”