L = int(input()) #방학일
A = int(input()) #국어숙제 페이지
B = int(input()) #수학숙제 페이지
C = int(input()) #국어 하루 숙제한계
D = int(input()) #수학 하루 숙제한계

if (A%C == 0) or (B%D == 0):
  print(L-max(A//C,B//D))
else:
  print(L-max(A//C+1,B//D+1))