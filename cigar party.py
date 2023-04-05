# cigar party
a=int(input("no. of cigar:"))
w=input("Y if weekend and N if not weekend:")
if((40<=a<=60 and w=='N') or (a>=40 and w=='Y')):
	print("True")
else:
	print("False")