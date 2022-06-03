n=int(input("Enter the number :"))
n1=n
sum=0
sum+=(n1%10)**3
n1/=10
n1=int(n1)
sum+=(n1%10)**3
n1/=10
n1=int(n1)
sum+=(n1%10)**3
sum=int(sum)
if sum==n:
    print("Armstrong number")
else : 
    print("Not a Armstrong number")