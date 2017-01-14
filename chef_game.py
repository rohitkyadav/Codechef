string = input("Enter a string")
c = h = e = f = 0

for letter in string :
    if letter =='C' :
        c += 1
    elif letter == 'H' and h<c :
        h += 1
    elif letter == 'E' and e<h :
        e += 1
    elif letter == 'F' and f<e :
        f += 1
print (f)