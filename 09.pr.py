a ="this.txt"
b ="copy.txt"

with open(a) as f:
    c = f.read()
with open(b) as f:
    d =f.read()

if c==d :
    print("yes this two files are identicle")
else:
    print("no these two files are not identicle")
