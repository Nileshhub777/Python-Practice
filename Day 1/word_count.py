def word_frequency(sentence):
    sentence=sentence.lower().replace(',','').replace('!','')
    words=sentence.split()

    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

text=input('Enter a sentence:')
print(word_frequency(text))




