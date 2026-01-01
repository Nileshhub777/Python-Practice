def lowercase_count(text):
    lower_string=""
    count=0
    for ch in text:
        if ch.islower():
            count+=1
            lower_string+=ch
    return count,lower_string

print(lowercase_count("Devops and Sre tech is quite GREAT"))