def ip_addr_extractor():
    Ip = []
    with open('abc.txt') as f:
        for line in f:
            for word in line.split():
                parts = word.split('.')
                if len(parts) == 4 and all(p.isdigit() for p in parts):
                    Ip.append(word)
    return Ip


print(ip_addr_extractor())