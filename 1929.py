import math

M,N = map(int, input().split())
prime = [True] * (N+1)
prime[0], prime[1] = False, False

for i in range(2, int(math.sqrt(N)) + 1) :
    for j in range(i*i, N+1, i) :
        if prime[i] :
            prime[j] = False

for i in range(M) :
    prime[i] = False

for i in range(N+1) :
    if prime[i] : 
        print(i, end="\n")