#identify type of character
a=input("enter the character")
if('a'<=a<='z' or 'A'<=a<='Z'):
	print("alphabet")
elif('0'<=a<='9'):
	print("digits")
else:
	print("special character")