for i in range(3):
  go_h, go_m, go_s, o_h, o_m, o_s = map(int, input().split())
  go_time = go_h * 3600 + go_m * 60 + go_s
  out_time = o_h * 3600 + o_m * 60 + o_s
  time = out_time - go_time
  hour = time // 3600
  min = time % 3600 // 60
  sec = time % 3600 % 60
  print("%d %d %d" %(hour, min, sec))