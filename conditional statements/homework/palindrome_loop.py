n=input("enter the number : ")
len_n=len(n)
s=int(n)
rev=0
i=1
while i<=len_n:
    rev*=10
    rev+=s%10
    s//=10
    i+=1

if str(rev)==n:
    print("palindrome")
else:
    print("not a palindrome")