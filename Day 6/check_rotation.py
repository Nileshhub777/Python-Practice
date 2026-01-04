def check_rotation(s1,s2):
    if len(s1) != len(s2):
        return False

    combined=s1+s1

    if s2 in combined:
        return True
    return False

print(check_rotation('abcde','cdeab'))