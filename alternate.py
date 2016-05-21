tests = int(input("Enter the number of tests: "))
while tests > 0:
	number = int(input("Enter the number of elements for a test: "))
	a = [int(x) for x in input().split()]

	for i in range(number):
		count1 = 0
		count2 = 0
		for j in range(3):
			if (a[i+j]<0 and a[i+j+1]>0):
				count1 += 1
			elif (a[i+j]>0 and a[i+j+1]<0):
				count2 += 1
			else:
				pass
		count = count1 + count2 + 1
		print(count)
	tests -= 1

