# 과락점수컷 10.5 7.5 12

t = int(input())
for _ in range(t) :
  num, s, m, t = map(int, input().split())
  if (s >= 10.5 and m >= 7.5 and t >= 12 and s+m+t >= 55) :
    print(num, s+m+t, "PASS")
  else :
    print(num, s+m+t, "FAIL")