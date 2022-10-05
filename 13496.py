test_case = int(input())
for i in range (test_case) :
  output = 0
  ships, speed, deadline = map(int, input().split())
  for _ in range (ships) :
    arrive, money = map(int, input().split())
    if arrive % speed != 0 :
      if (deadline >= (arrive // speed) + 1) :
        output += money
    else :
      if (deadline >= arrive // speed) :
        output += money
  print('Data Set %d:' %int(i+1))
  print(output)
  print()