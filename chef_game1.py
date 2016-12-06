def nb_move(s):
    c,h,e,f=0,0,0,0
    for i in range(0,len(s)):
         if s[i]=='C':
            c+=1
         elif s[i]=='H' and c>0:
             h=h+1
             c=c-1
         elif s[i]=='E' and h>0:
             e=e+1
             h=h-1
         elif s[i]=='F' and e>0:
             f=f+1
             e=e-1
    return f
 
print(nb_move(input()))   