c="a"
for i in range(1,6):
    for j in range(1,i+1):
        print(c,end=" ")
        c=chr(ord(c)+1)
    print()