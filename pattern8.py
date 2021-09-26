n=int(input("Enter no.: "))
for i in range(1,n+1):
	for j in range(1,n+1):
		if j<=i:
			print(str(j),end="")
		else:
			print("",end="")
	print()