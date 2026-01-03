def consonons(text):
    ctr = 0
    for each in text.lower():
        if each.isalpha() and each not in 'aeiou':
            ctr+=1
    return ctr

print(consonons('DevOps is GREAT'))

