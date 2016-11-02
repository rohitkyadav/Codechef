A = [2048,1024,512,256,128,64,32,16,8,4,2,1]
 
for _ in range(int(input())):
    N = int(input())
    i = 0
    C = 0
    while(N != 0):
        if( N >= A[i]):
            N -= A[i]
            C += 1
        else:
            i += 1
    print(C)