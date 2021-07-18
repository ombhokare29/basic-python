with open('a abuse_file.txt') as f:
    change =f.read()

change = change.replace('shit','****')

with open('a abuse_file.txt', 'w') as f:
    f.write(change)