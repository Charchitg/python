limit=int(input("enter the limit "))
last=-1
cur=1
i=1

next=last+cur
while next<=limit:
    print(next,end=" ")
    last,cur=cur,next
    next=cur+last
    i+=1
