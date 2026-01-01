def word_highest_count(a):
    result_dict = {}
    count = 0
    for word in a.split():
        if word not in result_dict:
            result_dict[word]=1
        else:
            result_dict[word]+=1

    max_count = 0
    max_word= ""
    for word in result_dict:
        if result_dict[word] > max_count:
            max_count=result_dict[word]
            max_word=word

    return max_count,max_word
print(word_highest_count("python is devops and SRE but devops more"))