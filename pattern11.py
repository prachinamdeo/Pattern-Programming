for i in range(1,6):
	print(i,end=" ")
print()
c=1
for i in range(5):
	if i == 0 or i == 4:
		print(2*c,end=" ")
		c+=1
	else:
		print("*",end=" ")
print()
c=1
for i in range(5):
	if i == 0 or i == 4:
		print((2*c)-1,end=" ")
		c+=1
	else:
		print("*",end=" ")
print()
for i in range(5,0,-1):
	print(i,end=" ")
print()

