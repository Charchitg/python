n1=int(input("enter the first number : "))
n2=int(input("enter the second number : "))
n3=int(input("enter the third number : "))
n4=int(input("enter the fourth number : "))
if n1<=n2 and n1<= n3 and n1<=n4:
    print(n1)
elif n2<=n1 and n2<=n3 and n2<=n4:
    print(n2)
elif n3<=n1 and n3<=n2 and n3<=n4:
    print(n3)
else:
    print(n4)