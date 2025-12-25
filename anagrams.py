def check_anagram(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if len(s1) != len(s2):
        return False

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False
    return True

print(check_anagram("listen","silent"))