numbers = list(map(int, input().split()))
numbers.sort()
for i in range (0,3):
  print(numbers[i], end=" ")