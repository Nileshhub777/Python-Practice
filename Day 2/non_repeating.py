def non_repeating_char(chr):

    for each in chr:
        if chr.count(each) == 1:
            return each
    return None

print(non_repeating_char("aaaabbncvvv"))