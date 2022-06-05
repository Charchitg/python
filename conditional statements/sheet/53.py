from re import I


n=int(input("enter the number : "))
sum=0
for i in range(1,n):
    if n%i==0:
        print(i,end=" ")
        sum+=i
print()
if sum == n:
    print("perfect number ")
else :
    print("not a perfect number")

