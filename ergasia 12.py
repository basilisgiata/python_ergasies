from datetime import date
from datetime import datetime
from calendar import monthrange

#inputs
d=int(input("Enter day "))
m=int(input("Enter month "))
y=int(input("Enter year "))
d1=date((y),m,d)

now = datetime.now()
d0=date((now.year),(now.month),(now.day))
delta = d1 - d0


s1 = now.strftime("%H:%M:%S")
s2 = '00:00:00' 
FMT = '%H:%M:%S'


if d1<d0:
    tdelta = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
    print (tdelta + delta,"since",d1.strftime("%d/%m/%Y"))
else:
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print (tdelta + delta,"until",d1.strftime("%d/%m/%Y"))

x=monthrange(y,m)
print ("This month has ",x[1],"days")
