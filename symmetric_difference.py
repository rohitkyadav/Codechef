"""
Given  sets of integers, M and N , print their symmetric difference in ascending order. The term 
symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

M = input()
m = input().split()
N = input()
n = input().split()

print ("\n".join(sorted(list(set(m) ^ set(n)),key=int)))

# another solution
"""
M = int(input())
L1 = [int(x) for x in input().split()]
N = int(input())
L2 = [int(x) for x in input().split()]

for x in L1:
	if x not in L2:
		print(x)
for x in L2:
	if x not in L1:
		print(x)
"""