# python3 -> pypy3

import math

# 에라토스테네스의 체로 소수 구하기
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]  # 소수 리스트 반환

# 소수 리스트를 한번만 구하기
MAX_LIMIT = 1000000
primes = sieve_of_eratosthenes(MAX_LIMIT)
prime_set = set(primes)  # 빠른 소수 확인을 위해 set으로 변환

# 입력을 받아 처리하는 부분
while True:
    n = int(input())
    if n == 0:
        break
    
    # 골드바흐의 추측을 만족하는 두 소수를 찾습니다.
    for i in primes:
        if i > n // 2:  # i가 n/2을 넘으면 더 이상 검사할 필요 없음
            break
        if (n - i) in prime_set:  # n-i가 소수이면
            print(f"{n} = {i} + {n - i}")
            break
