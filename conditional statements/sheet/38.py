n1=int(input("enter marks of first subject(out of 100) : "))
n2=int(input("enter marks of second subject(out of 100) : "))
n3=int(input("enter marks of third subject(out of 100) : "))
avg=(n1+n2+n3)/3
if n1>75 and n2>75 and n3>75 and avg>80:
    print("pass")
else:
    print("fail")