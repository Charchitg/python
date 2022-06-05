start=int(input("enter the starting limit : "))
end=int(input("enter the ending limit : "))
prime=[]

for i in range(start,end+1,1):
    j,flag=2,True 
    while j**2 <= i:
        if i%j == 0:
            flag=False
            break
        j+=1
    if flag:
        prime.append(i)


print(prime)
        