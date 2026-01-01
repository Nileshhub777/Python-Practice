def empty_file_handle():
    try:
        with open('emp_file.txt', 'r') as f:
            content = f.read()
            if content.strip() == "":
                return 'It is a empty file.'
        return content

    except FileNotFoundError:
        return 'File not found'

print(empty_file_handle())