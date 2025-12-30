def error_extract_lines():
    with open('abc.txt') as inline:
        with open('xyz.log','w') as outfile:
            for line in inline:
                if line.startswith('ERROR'):
                    outfile.write(line)
    return outfile

print(error_extract_lines())



# Both files are safely opened and closed automatically.