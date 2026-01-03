def count_vowels(text):
    count=0
    for each in text.lower():
        if each in 'aeiou':
            count+=1
    return count

print(count_vowels('hellosuperbman'))