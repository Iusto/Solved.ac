import sys
i = int(sys.stdin.readline())

for _ in range (i) :
  a,b = sys.stdin.readline().split()
  if a == b :
    print("OK")
  else :
    print("ERROR")
