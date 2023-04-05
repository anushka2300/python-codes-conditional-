#driving bike
a=int(input("enter the speed:"))
bday=input("Y if its ur bday else input N")
if((a<60 and bday=='N') or (a<65 and bday=='Y')):
	print("Card 1")
elif((61<=a<=80 and bday=='N') or (66<=a<=85 and bday=='Y')):
	print("Card 2")
elif((a>=81 and bday=='N') or (a>=86 and bday =='Y')):
	print("card 2")