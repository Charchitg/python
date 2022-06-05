

# A
# AB
# ABC
# ABCD


for i in range(1,5):
    c="A"
    for j in range(1,i+1):
        print(c,end=" ")
        n=ord(c)
        n+=1
        c=chr(n)
    print()