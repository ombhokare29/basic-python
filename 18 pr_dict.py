hindi={
    "fan" : "pankha",
   "human" : "insaan",
   "women" : "stree",
   "door": "darvaja",
   "pen": "kalam",
   "stone": "patthar",

}
print("the options are :", hindi.values())
a= input("enter the english word:\n")
print("the meaning of the word you entered is:")
print(hindi.get(a))
# print(hindi[a]) # it will throw error for the nword not in the dictionary
