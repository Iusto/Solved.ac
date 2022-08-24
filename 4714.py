import sys
while True :
  i = float(sys.stdin.readline())
  if i < 0 : 
    quit()
  moon = i * 0.167
  print('Objects weighing %.2f on Earth will weigh %.2f on the moon.' %(i, moon))