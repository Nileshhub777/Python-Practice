def find_duplicate_words():
    word_count = {}
    with open('abc.txt','r') as f:
        for line in f :
            for word in line.split():
                if word in word_count:
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1
    duplicate_words=[]

    for key in word_count:
        if word_count[key] > 1:
            duplicate_words.append(key)
    return duplicate_words
print(find_duplicate_words())