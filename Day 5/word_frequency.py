def word_frequency(text):
    result = {}

    for word in text.split():
        if word in result:
            result[word] +=1
        else:
            result[word] = 1
    return result

print(word_frequency("python devops python"))