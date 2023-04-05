#category of customer
a=eval(input("enter the amount"))
if(a>25000):
	print("GOLD")
	a=a*(20/100)
	print("amount to be paid is",a)
	
elif(a>10000 and a<=25000):
	print("SILVER")
	a=a*(10/100)
	print("amount to be paid is",a)
	
else:
	print("BRONZE")
	a=a*(5/100)
	print("amount to be paid is",a)
	
	
	