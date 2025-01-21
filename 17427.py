# 17427번 약수의 합 2

# 약수 구하기
n = int(input())
sum = 0

for i in range(1, n+1):
    # i의 배수 개수 = i를 약수로 가지고 있는 수의 개수
    sum += (n//i) * i
# 정답
print(sum)