T = int(input("enter the number of tests: "))

while T>0:
	N, K = map(int, input("Enter the values of N and K: ").split())
	print("Enter the list of strings here: ")
	D = [str(x) for x in input().split()]
	S = []
	
	for x in range(K):
		L = int(input("Enter the number of strings in each K: "))
		for y in range(L):
			y = input("Enter the string: ")
			S.append(y)
	S = set(S)	
	
	for x in range(len(D)):
		if D[x] in S:
			print("YES", end=' ')
		else:
			print("NO", end=' ')
	print("\n")
	T -= 1