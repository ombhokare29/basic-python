def remove_and_split(string, word):
    newstr= string.replace(word, "")
    return newstr.strip()

a= ("    om is a very good boy    ")
print(remove_and_split(a , "very"))