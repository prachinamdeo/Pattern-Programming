n=int(input("Enter no. : "))
for i in range(1,n+1):
	for j in range(n,0,-1):
		if i>= j:
			print(j,end="")
		else:
			print("",end="")
	print()