change=['shit' ,'kaddu','idiot','stupid','fool']

with open('a abuse_file.txt') as f:
    newFile =f.read()

    for a in change:
        newFile=newFile.replace(a, "*****")
        with open ('a abuse_file.txt','w') as f:
            f.write(newFile)
