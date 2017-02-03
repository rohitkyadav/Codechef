import datetime

t = int(input())

while (t):
    year = int(input())
    day = datetime.date(year,1,1).strftime("%A")
    print (day.lower())
    t = int(t) - 1 