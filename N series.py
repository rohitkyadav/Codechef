import math

T = int(input())

while (T>0):
	sum = 0
	n = int(input())
	for x in range (1, n+1):
		sum += (math.pow(x, 2) - math.pow(x-1, 2))

	print(int(sum % (math.pow(10, 9) + 7)))
	T -= 1