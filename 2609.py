a, b = map(int, input().split())

# 유클리드 알고리즘을 사용하여 최대공약수 구하기
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# 최소공배수 계산
gcd_value = gcd(a, b)
lcm = abs(a * b) // gcd_value

print(gcd_value)
print(lcm)
