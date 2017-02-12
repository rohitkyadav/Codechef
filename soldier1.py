soldiers = int(input("Enter the no. of soldiers: "))
list = []
odd = 0
even = 0

for x in range(soldiers):
	number = int(input("Enter the no. on soldier's gun: "))
	list.append(number)

for x in range(soldiers):
	if (list[x] % 2 == 0):
		even += 1 
	else:
		odd += 1

if even > odd:
	print("READY FOR BATTLE")
else:
	print("NOT READY")