def return_key_value(data,key):
    if key in data:
        return data[key]

print(return_key_value({'env':'prod','region':'EU'}, 'env'))