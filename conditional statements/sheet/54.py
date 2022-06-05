n=int(input("enter the number of inputs : "))
evenlist=[]
oddlist=[]
even=0
odd=0
for i in range(0,n):
    x=int(input("enter the number "))
    if x%2==0:
        even+=1
        evenlist.append(x)
    else:
        odd+=1
        oddlist.append(x)

print("number of even numbers =" , even , "number of odd numbers are :" , odd)
print(evenlist)
print(oddlist)