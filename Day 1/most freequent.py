def most_freq(element):
    max_count=0

    for item in element:
        count=element.count(item)
        if count>max_count:
            max_count=count
    return item

print(most_freq([1,2,2,2,3,3,4,4,4,5,6,6,6,6,6]))