def Count(len):
  cnt = 1
  ep = maguk[0]
  for i in range(1, n):
    if maguk[i] - ep >= len:
      cnt += 1
      ep = maguk[i]
  return cnt
  
n, c = map(int, input().split())
maguk = [int(input()) for _ in range(n)]

maguk.sort()
lt = 0
rt = max(maguk)
start = min(maguk)
last = max(maguk)
res = 0

while lt <= rt:
  mid = lt + rt // 2
  if Count(mid) >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1
    
print(res)  

