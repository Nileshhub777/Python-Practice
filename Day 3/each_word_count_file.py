def each_word_count_file():
    with open("abc.txt") as f:
        dic1={}
        for line in f:
            for word in line.split():
                if word not in dic1:
                    dic1[word]=1
                else:
                    dic1[word]=dic1[word] + 1
        return dic1

print(each_word_count_file())