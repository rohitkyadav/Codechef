T = int(input())

while T>0:
	N, K = map(int, input().split())
	D = [str(x) for x in input().split()]
	S = []
	for x in range(K):
		phrase = [str(x) for x in input().split()]
		S += phrase
	S = set(S)	
	for x in D:
		if x in S:
			print("YES", end=' ')
		else:
			print("NO", end=' ')
	print("\n")
	T -= 1