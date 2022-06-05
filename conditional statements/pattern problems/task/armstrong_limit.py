start=int(input("enter the starting limit : "))
end=int(input("enter the ending limit : "))
armstrong=[]

for i in range(start,end+1,1):
    sum=0
    n=i
    cnt=len(str(n)) 
    while n!=0:
        sum+=(n%10)**cnt
        n//=10        
    if i==sum:
        armstrong.append(i)


print(armstrong)
        