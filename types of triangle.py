#to find whether triangle is scalene,right or isosceles
a=int(input("enter 1st side"))
b=int(input("enter 2nd side"))
c=int(input("enter 3rd side"))
if(a!=b and b!=c and c!=a):
	print("scalene triangle")
	flag=1
if(a==b or b==c or c==a):
	print("isosceles triangle")
	flag=1
	
if((a**2 + b**2 == c**2 ) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2)):
	print("right angled triangle")
	flag=1
if(flag!=1):

	print("invalid")