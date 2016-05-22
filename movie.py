T = int(input("Enter the number of tests: "))

while T>0:
	P = []
	N = int(input("Enter the number of movies: "))
	print("Enter the length of each movie")
	L = [int(x) for x in input().split()]
	print("Enter the rating of each movie")
	R = [int(x) for x in input().split()]
	for x in range(N):
		p = L[x] * R[x]
		P.append(p)
	M = max(P)
	N = max(R)
	for x in P:
		c1 = P.count(M)
	for x in R:
		c2 = R.count(N)
	if c1>1 and c2>1:
		I = R.index(N)
		print(I + 1)
	elif c1>1:
		I = R.index(N)
		print(I + 1)
	else:
		print(M)
	T -= 1
