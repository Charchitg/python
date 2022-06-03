s=input("enter the uppercase or lowercase alphabet ")
n=ord(s)
if n >= 65 and n <= 90:
    print("Uppercase")
elif n >= 92 and n<=122:
    print("lowercase")
else:
    print("invalid")