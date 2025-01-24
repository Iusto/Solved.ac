import math

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 입력 처리
T = int(input())  # 입력 숫자의 개수
num = list(map(int, input().split()))  # 숫자들 입력받기

# 소수 개수 세기
prime_count = 0
for i in num:
    if is_prime(i):
        prime_count += 1

print(prime_count)
