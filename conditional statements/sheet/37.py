last=int(input("enter the units of last month : "))
cur=int(input("enter the units of current month : "))
used=cur-last
if used>=0 and used<=100:
    price=2*used
elif used>=101 and used<=200:
    price=3*used
elif used>=201 and used<=300:
    price=4*used
elif used>300:
    price=5*used
print("your current electricity bill is Rs." , price)

