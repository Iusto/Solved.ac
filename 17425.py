# python3이 아니라 pypy3으로 실행해야 시간초과가 안남 (pypy3이  캐싱을 지원)
# dp[j] += i와 같은 반복문이 자주 실행되므로, JIT가 이 부분을 최적화하여 성능을 크게 향상
# pypy3이 캐싱 및 JIT 컴파일을 통해 성능을 최적화

import sys

input = sys.stdin.readline

MAX = 1_000_001
dp = [0] * MAX
for i in range(1, MAX):
    for j in range(i, MAX, i):
        dp[j] += i

prefix_sum = [0] * MAX
for i in range(1, MAX):
    prefix_sum[i] = prefix_sum[i - 1] + dp[i]
    
answer = []
for _ in range(int(input())):
    n = int(input())
    answer.append(str(prefix_sum[n]))

print("\n".join(answer))
