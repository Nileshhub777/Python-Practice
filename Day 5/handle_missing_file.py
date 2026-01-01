def handle_missing_file(filename):
    try:
        with open(filename,'r') as f:
            return f.read()
    except FileNotFoundError:
        return 'File not found'

print(handle_missing_file('xyw.txt'))


# Production systems must fail gracefully.