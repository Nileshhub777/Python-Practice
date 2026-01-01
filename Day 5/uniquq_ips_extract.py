def unique_ip_address():
    ip_list=set()
    with open('abc.txt','r') as f:
        for line in f:
            for word in line.strip().split():
                parts = word.split('.')
                if len(parts)==4 and all(p.isdigit() for p in parts):
                    ip_list.add(word)
    return ip_list
print(unique_ip_address())

# I used a set because IP addresses should be unique and sets handle uniqueness efficiently.