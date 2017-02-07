for _ in range(int(input())):
	n = int(input())
	l, r = list(map(int,input().split())), list(map(int,input().split()))
	mp, mr, idx = 0, 0, 0
	
	for i in range(n):
		if l[i]*r[i] > mp:
			mp = l[i]*r[i]
			mr = r[i]
			idx = i+1
		elif l[i]*r[i] == mp:
			if r[i] > mr:
				mr = r[i]
				idx = i+1
	print(idx)
