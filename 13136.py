R,C,N = map(int, input().split())
if R%N != 0 :
  Rout = R//N + 1
else :
  Rout = R//N

if C%N != 0 :
  Cout = C//N + 1
else :
  Cout = C//N

print(Rout*Cout)