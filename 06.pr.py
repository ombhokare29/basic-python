with open('log.txt') as f:
    file=f.read()

if 'python' in file.lower():
    print('python is present')
else:
    print("python is not present")