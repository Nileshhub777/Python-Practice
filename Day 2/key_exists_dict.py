def key_existing_dict(dict,key):

    if key in dict:
        return True

print(key_existing_dict({"env": "prod", "region": "eu"}, 'env'))