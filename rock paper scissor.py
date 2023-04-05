#rock paper scissor
a=input("name 1")
b=input("name 2")
x=input("choice 1")
y=input("choice 2")
if((x=="rock" and y=="scissor") or (x=="scissor" and y=="paper") or (x=="paper" and y=="rock")):
	print("player 1 is winner")
else:
	print("player 2 is winner")