def count_words():
    count=0
    with open('abc.txt') as f:
        for each in f :
            count=count + each.lower().count('devops')
    return count

print(count_words())


# “I read the file line by line and count occurrences of the word using string count.”