n=input("Enter the number : ")
n1=""
n2=int(n)
n3=n2%10
n1+=str(n3)
n2=int(n2/10)
n3=n2%10
n1+=str(n3)
n2=int(n2/10)
n3=n2%10
n1+=str(n3)
n2=int(n2/10)

if n1==n:
    print("palindrome ")
else :
    print("not a palindrome")
