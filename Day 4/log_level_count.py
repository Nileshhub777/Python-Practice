def log_level_count():
    log_level={}
    with open('abc.txt','r') as f:
        for line in f:
            level=line.split()[0]
            if level in log_level:
                log_level[level]+=1
            else:
                log_level[level]=1
    return log_level
print(log_level_count())