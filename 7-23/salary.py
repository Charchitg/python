bs=input("enter the base salary : ")
bs=float(bs)
ta=0.1*bs
pf=0.078*bs
da=500
gs=bs+ta+da
print("gross salary : ",gs)
ns=gs-pf
print("nett salary : " , ns)