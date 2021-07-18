file = True
i= 1
with open('log.txt') as f:
    while file:
        file = f.readline()
        if "python" in file.lower():
            print(f'python is present in the line number {i} ')
        i+=1