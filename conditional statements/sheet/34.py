bs=int(input("enter the basic salary : "))
if bs>=0 and bs<=10000:
    ta=0.1*bs
    da=0.05*bs
else:
    ta=0.12*bs
    da=0.06*bs
gs=bs+ta+da
print(gs)