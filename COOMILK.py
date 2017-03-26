# program

T = int(input())
while T:
	N = int(input())
	S = list(map(str,input().strip().split()))
	
	if(S[N-1]=='cookie'):
	    followed = "NO"
    
    else:
        for x in range(0, N-1):
            if(S[x] == "cookie" and S[i+1] != "milk"):
                followed = "NO"
                break
            
            followed = "YES"
    print(followed)