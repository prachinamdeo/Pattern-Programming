print("Pascal Triangle")
n=5
i=0
for j in range(n,0,-1):
    ns="" 
    print(" "*j,end="")
    s=str(11**i)
    for k in s:
        ns=ns+k+" "
    print(ns)
    i+=1