H = int(input()) #상근
M = int(input()) #중근
L = int(input()) #하근
Coke = int(input()) #콜라
Soda = int(input()) #사이다

Hamberger = []
Hamberger.append(H)
Hamberger.append(M)
Hamberger.append(L)

beverage = []
beverage.append(Coke)
beverage.append(Soda)

Hamberger.sort()
beverage.sort()

print(Hamberger[0]+beverage[0]-50)