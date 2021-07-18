# n= 5
# product =1
# for i in range(n):
#     product = product * (i+1)
# print(product) 
def factorial_i(n):
    product= 1
    for i in range(n):
        product= product*(i+1)
    return product

def factorial_r(n):
    # if n==1 or n==0 :
        # return 1
    return n*factorial_r(n-1)


print(factorial_r(5))
