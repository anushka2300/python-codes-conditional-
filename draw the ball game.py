print("***WELCOME TO THE PICK UP GAME***")
print("RULES")
print("Draw less than 5 balls from the basket")


flag=0
a=51
while(a>0):
	if(a>0):
		u=int(input("draw the balls:"))
		a=a-u
		flag=1
	if(a>0):
		
		print("draw the ball bot:",end=' ')
		if(u==1):
			comp=4
		elif(u==2):
			comp=3
		elif(u==3):
			comp=2
		elif(u==4):
			comp=1
		print(comp)
		flag=2
	a=a-comp
	print("balls left:",a)
		
	
if(flag==1):
	print("winner is computer")
elif(flag==2):
	print("winner is user")