s=input("enter the alphabet : ")
n=ord(s)
if n>=65 and n<=90:
    n+=32
else:
    n-=32
s=chr(n)
print(s)