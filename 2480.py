temp = input().split(" ")
list = []
for i in temp:
  list.append(int(i))
list.sort()
list_1 = set(list)

if len(list_1) == 3: # 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원
  print(list[-1]*100) 
elif len(list_1) == 1: # 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원
  print(10000+list[1]*1000)
else: # 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원
  print(1000+list[1]*100)