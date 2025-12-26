def check_palindrome(s):
    if s.lower() == s.lower()[::-1]:
        print("Palindrome")
        return True
    else:
        print("Not Palindrome")
        return False

print(check_palindrome("Madame"))