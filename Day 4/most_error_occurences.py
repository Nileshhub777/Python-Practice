def most_error_occurences():
    error_dict={}
    with open('abc.txt','r') as f:
        for line in f:
            if line.startswith('ERROR'):
                err_msg=line.strip().split(' ',1)[1]

                if err_msg in error_dict:
                    error_dict[err_msg]+=1
                else:
                    error_dict[err_msg]=1

    max_count =0
    max_error=None

    for e,c in error_dict.items():
        if c > max_count:
            max_count=c
            max_error=e
    return max_error, max_count

print(most_error_occurences())