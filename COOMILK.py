"""
Limak is a little polar bear, who loves eating cookies and drinking milk. For this reason he often 
visits Chef's kitchen.

Limak is going to spend N minutes in the kitchen. Each minute he either eats a cookie or drinks 
milk. Cookies are very sweet and thus Limak's parents have instructed him, that after eating a 
cookie, he has to drink milk in the next minute.

You are given whether he ate a cookie or drank milk in each of the N minutes. Your task is to check
if Limak followed his parents' instructions. That is, you need to verify whether after each eaten 
cookie he drinks milk in the next minute. Print "YES" or "NO" for each test case accordingly.

Input
The first line of the input contains an integer T denoting the number of test cases. The description 
of T test cases follows.

The first line of each test case contains an integer N denoting the number of minutes.

The second line of a test case contains N space-separated strings S1, S2, ..., SN. The string Si 
is either "cookie" (if Limak eats a cookie in the i-th minute) or "milk" (otherwise).

Output
For each test case, output a single line containing the answer — "YES" if Limak followed his 
parents' instructions, and "NO" otherwise, both without the quotes.


Example

Input:
4
7
cookie milk milk cookie milk cookie milk
5
cookie cookie milk milk milk
4
milk milk milk milk
1
cookie

Output:
YES
NO
YES
NO
"""
# program

T = int(input())
while T:
	N = int(input())
	S = list(map(str,input().strip().split()))

	if(S[N-1]=='cookie'):
		followed = "NO"
    
	else:
		for x in range(0, N-1):
			if(S[x] == "cookie" and S[x+1] != "milk"):
				followed = "NO"
				break

			followed = "YES"
	print(followed)

	T -= 1

# another solution

# T = int(input())
# while T:
# 	N = int(input())
# 	S = list(map(str,input().strip().split()))
	
# 	if 'cookie cookie' in S or S.endswith('cookie'):
# 		print ("NO")
# 	else:
# 		print("YES")
# 	T -= 1