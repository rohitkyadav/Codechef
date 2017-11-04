T = int(input())
while T:
	N, P = map(int, input().split())
	solving = [int(x) for x in input().split()]
	c, f = 0, 0

	for x in solving:
		if x <= int(P/10):
			c += 1
		if x >= int(p/2):
			f += 1

	if  c==1 and h==2:
		print("yes")
	else:
		print("no")
	T -= 1