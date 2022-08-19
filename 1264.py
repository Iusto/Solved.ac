while True:
  data = input()
  if (data == '#'):
    break
  result = 0
  value = ['a','e','i','o','u','A','E','I','O','U']
  for i in range (len(data)): #data 길이만큼
    if data[i] in value : #data[0~length까지] value와 비교
      result += 1         #Ex) 1 in [1, 2, 3] True
  print(result)