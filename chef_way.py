N, K = map(int, input("Enter the numbers: ").split())
a = [int(x) for x in input().split()]
l = []

for x in range(1, N):
	p = a[0]*a[N-1]
	if a[x]*a[0]<=K and a[x]*a[0]>1:
		p = p*a[x]
		l.append(p)
	else:
		pass
O = min(l or ['empty list'])
print(O)
