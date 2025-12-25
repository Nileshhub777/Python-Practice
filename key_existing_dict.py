def key_dictionary(data,key):

    return key in data

print(key_dictionary({"env": "prod", "region": "eu"},'env'))
