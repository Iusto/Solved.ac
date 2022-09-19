num = int(input())
num_li = list(map(int, input().split()))
count = 0

for i in num_li :
  if i == num :
    count += 1

print(count)