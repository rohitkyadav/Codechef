T = int(input())
while T:
	N, M = map(int, input().split())
	while M:
		u, v = map(int, input().split())
		M -= 1
	if N%2==0:
		print("yes")
	else:
		print("no")

	T -= 1