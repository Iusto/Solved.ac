test, length = map(int, input().split())
for i in range (test) :
  num = input()
  if len(num) > length : break
  print(num[::-1])