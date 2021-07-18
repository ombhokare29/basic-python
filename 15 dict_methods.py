mydict={
    "om":"a clever boy",
    "ipl":"RCB",
    "krishna":"nibba",
    "dict2" : {'heaven' : 'JNV',
    'krishna': 'power hitter'},
    1:4
}
print(list(mydict.keys()))
print(list(mydict.values()))
# print(mydict.keys) error... must keep list before mydict
print(mydict.items())
print(mydict)
dict_update = {
    "divya" : "a girl" ,
    "omkar" : "a boy" ,
    "gas " : "cylinder",
    "om" : "bodygaurd"
}
mydict.update(dict_update)
print(mydict)
# print(mydict["omkar1"])
# throws  a key  error  because omkar1 is  not present in the dictionary...
# therefore we will use .get function to avoid the error
print(mydict.get("omkar1"))
print(type(mydict))