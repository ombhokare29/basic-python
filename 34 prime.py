num =int(input('Enter the number:  '))
prime = True

for i in range(2 , num):
    if (num%i==0):
        prime = False
        break
if prime:
    print("Yes, this number is prime.")
else:
    print("No, this number is not prime.")
