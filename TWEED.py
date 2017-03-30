T = int(input());
while(T):
	N, P = input().split()
	M = [int(x) for x in input().split()]
	N = int(N)
	
	if (N==1 and M[0]%2 == 0 and P=="Dee"):
		print("Dee")
	else:
		print("Dum")

	T -= 1