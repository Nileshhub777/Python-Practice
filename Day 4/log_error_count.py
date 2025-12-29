def log_level_error_only():
    ctr = 0
    with open('abc.txt', 'r') as f:
        for line in f:
            level = line.split()[0]
            if level == 'ERROR':
                ctr += 1
    return ctr


print(log_level_error_only())
