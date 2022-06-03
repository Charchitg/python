first=input("enter the marks of first subject : ")
second=input("enter the marks of second subject : ")
third=input("enter the marks of third subject : ")
fourth=input("enter the marks of fourth subject : ")
fifth=input("enter the marks of fifth subject : ")

#typecasting to int

first=int(first)
second=int(second)
third=int(third)
fourth=int(fourth)
fifth=int(fifth)

percentage=(first+second+third+fourth+fifth)/500
percentage=percentage*100
print("percentage out of 500 = " , percentage , "%")