inf, math, sci, eng = map(int, input().split())
inf2, math2, sci2, eng2 = map(int, input().split())
S = inf + math + sci + eng
T = inf2 + math2 + sci2 + eng2
if S == T:
  print(S)
else:
  print(max(S,T))