a = int(input())
b = int(input())
c = int(input())
d = int(input())
#-------------------
e = int(input())
f = int(input())

sci = []
sci.append(a)
sci.append(b)
sci.append(c)
sci.append(d)
sci.sort(reverse=True)
print(sum(sci[0:3:]) + max(e,f))