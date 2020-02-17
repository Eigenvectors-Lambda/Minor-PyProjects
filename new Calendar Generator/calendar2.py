import calendar

y=int(input("Enter the Year:"))
m=1
print("\n---------Calendar----------")
Cal=calendar.TextCalendar(calendar.MONDAY) 

i=1

while i<=12:
    Cal.prmonth(y,i)
    i+=1
