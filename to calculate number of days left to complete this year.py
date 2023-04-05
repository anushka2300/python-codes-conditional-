#to find the number of days left from current date
import datetime
d=int(input("enter todays date:"))
m=int(input("enter current month"))
a=datetime.date(2023,m,d)
b=datetime.date(2023,12,31)
left=b-a
print("number of days left is",left)