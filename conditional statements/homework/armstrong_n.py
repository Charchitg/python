n=input("enter the number : ")
s=len(n)
n1=int(n)
n=int(n)
sum=0
while n1!=0:
    sum+=(n1%10)**s
    n1//=10

if sum==n:
    print("Armstrong")
else:
    print("not a armstrong")  