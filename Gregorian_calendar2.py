
import calendar
t=int(input())
l=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']        
while(t):
    j=int(input())
    c=calendar.weekday(j,1,1)
    print(l[c])
    t-=1  