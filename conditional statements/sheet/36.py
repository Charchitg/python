n1=int(input("enter marks of first subject (out of 100) : "))
n2=int(input("enter marks of second subject (out of 100) : "))
n3=int(input("enter marks of third subject (out of 100) : "))
n4=int(input("enter marks of fourth subject (out of 100) : "))
n5=int(input("enter marks of fifth subject (out of 100) : "))
sum=n1+n2+n3+n4+n5
per=sum/5
if per>=60:
    grade="A"
elif per>=50:
    grade="B"
elif per>=40:
    grade="C"
else:
    grade="D"
print("grade = " , grade , "\npercentage = " , per)