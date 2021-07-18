s1=int(input("Enter your marks s1\n"))
s2=int(input("Enter your marks s2\n"))
s3=int(input("Enter your marks s3\n"))
avg=(s1+s2+s3)/3
if (s1<33 or s2<33 or s3<33):
    print("you are fail beacause of less marks in eigther sub")
elif avg>=40 :
    print("pass")
else:
    print("fail")