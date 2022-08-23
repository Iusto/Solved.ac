i = int(input())
li = []
print('Gnomes:')
for _ in range (1,i+1) :
  a,b,c = map(int,input().split())
  li.append(a)
  li.append(b)
  li.append(c)
  if (li[0] < li[1] and li[1] < li[2]) or (li[0] > li[1] and li[1] > li[2]) :
    print('Ordered')
  else : print('Unordered')
  li.remove(a)
  li.remove(b)
  li.remove(c)