def word_freq(sentence):
    output={}
    words=sentence.split()

    for each in words:
        if each in output:
            output[each]=output[each]+1
        else:
            output[each]=1
    return output

print(word_freq('apple is a fruit and fruit is a good to eat'))