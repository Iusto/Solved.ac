import sys
while True :
  name, age, weight = sys.stdin.readline().split()
  age, weight = int(age), int(weight)
  if (name == '#' and age == 0 and weight == 0) :
    quit()
  if (age > 17 or weight >= 80) :
    print('%s Senior' %name)
  else : print('%s Junior' %name)