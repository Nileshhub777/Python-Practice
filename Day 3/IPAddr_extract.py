def ip_address_extract():
    list1=[]
    with open('abc.txt') as f:
        for line in f:
            for word in line.split():
                parts = word.split('.')
                if len(parts) == 4:
                    list1.append(word)
    return list1
print(ip_address_extract())




# “I check each word; only those that look like four dot-separated numbers are kept. Others are ignored automatically.”