n=int(input("enter the 3 digit number : "))
n1=int(n%10)
n/=10
n2=int(n%10)
n/=10
n3=int(n%10)
if n1>=n2 and n1>=n3:
    print(n1)
elif n2>=n1 and n2>=n3:
    print(n2)
else:
    print(n3)