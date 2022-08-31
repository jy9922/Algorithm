def Count(len):
  cnt = 0
  for i in m:
    if abs(i - len) >= len:
      cnt += 1
      i = mid
  return cnt
    

n, c = map(int, input().split())
m = [int(input()) for _ in range(n)] 

m.sort()
lt = min(m)
rt = max(m)

while lt <= rt:
  mid = (lt+rt)//2
  if Count(mid) < c:
    rt = mid - 1
  else:
    lt = mid + 1

print(mid)
