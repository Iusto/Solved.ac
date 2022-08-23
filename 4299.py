plus,minus = map(int,input().split())
if plus-minus < 0 or (plus-minus)%2!=0:
    print(-1)
else:
    b=(plus-minus)//2
    a=plus-b
    print(max(b,a),min(a,b))