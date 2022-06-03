from re import I


n=int(input("enter the number :"))
fact=1
i=1
while i<=n:
    fact*=i 
    i+=1
print("factorial of n = " ,n , " : " , fact )