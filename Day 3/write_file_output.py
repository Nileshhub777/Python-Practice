def file_output_writing():
    with open('abc.txt','r') as inline:
        with open('xyz.txt','w') as outfile:
            for line in inline:
                outfile.write(line.upper())
 #           outfile.write(inline.read().upper())
file_output_writing()