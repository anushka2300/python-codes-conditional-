# prime number in given range
a=int(input("enter upper range:"))
b=int(input("enter lower range:"))

for i in range(b,a):
	c=0
	for j in range(1,i+1):
		if(i%j==0):
			c+=1
	if c==2:
		print(i)
		
	
			
		