def print_dict(data):
    for key,value in data.items():
        print(key, value)
print(print_dict({"env": "prod", 'region':'Dev'} ))


# I use dict.items() to loop through keys and values together.
# It’s clean and avoids calling dict[key] separately.”