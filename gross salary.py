#calculate gross salary
sal=int(input("enter basic salary"))
if(sal<=10000):
	sal=sal+sal*(20/100)+sal*(80/100)
elif(sal>10000 and sal<=20000):
	sal=sal+sal*(25/100)+sal*(90/100)
else:
	sal=sal+sal*(30/100)+sal*(95/100)
print(sal)