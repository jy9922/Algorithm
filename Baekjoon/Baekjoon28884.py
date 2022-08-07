h, m = map(int, input().split())

time = h * 60 + m - 45

# 시 단위로 나누기.
h = time // 60 
if h < 0:
  h += 24
m = time % 60

print(h, m)
