def check_anagram(word1,word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        return False

    for ch in word1:
        if word1.count(ch) != word2.count(ch):
            return False
    return True
print(check_anagram("Listen","Silent"))
