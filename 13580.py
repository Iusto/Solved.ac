a,b,c = map(int, input().split())
li = []
li.append(a)
li.append(b)
li.append(c)
li.sort()
if(li[0] == li[1] or li[1] == li[2] or li[0] + li[1] == li[2]) :
  print("S")
else :
  print("N")
  