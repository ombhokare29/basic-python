letter = ''' dear, |<NAME>|,
you are selected! congratulations for your excellent performance in the examination.
|<DATE>|
'''
NAME =input("enter your name\n")
DATE = input("enter the date\n")
letter = letter.replace("|<NAME>|",NAME)
letter = letter.replace("|<DATE>|", DATE)
print(letter)
# replaces all the terms...
