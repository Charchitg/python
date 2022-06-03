l=int(input("enter the length of rectangle : "))
b=int(input("enter the breadth of rectangle : "))
perimeter=2*(l+b)
area=l*b
if perimeter > area:
    print("perimeter is greater")
elif perimeter==area:
    print("Equal area and perimeter") 
else:
    print("area is greater")