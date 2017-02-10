soldiers = int(input("Enter the no. of soldiers: "))
odd = 0
even = 0
list = [int(x) for x in input().split()]

for x in range(soldiers):
	if (list[x] % 2 == 0):
		even += 1 
	else:
		odd += 1

if even > odd:
	print("READY FOR BATTLE")
else:
	print("NOT READY")