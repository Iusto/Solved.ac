a,b,c = map(int, input().split())
li = []
li.append(a)
li.append(b)
li.append(c)
li.sort()

if (li[0] == li[1] == li[2]) :
  print("2")
elif (li[0]**2 + li[1]**2 == li[2]**2) :
  print("1")
else : print("0")