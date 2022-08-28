n, m = map(int, input().split())
dvd = list(map(int, input().split()))

lt = 0
rt = sum(dvd)
total = 0
cnt = 0
res = 1000

while lt <= rt:
  mid = (lt+rt)//2
  for i in dvd:
    total += i
    if total > mid:
      cnt += 1
      total = i
  cnt += 1
  if cnt < m:
    rt = mid - 1
  elif cnt > m:
    lt = mid + 1
  elif cnt == m:
    rt = mid - 1
    res = min(res, mid)
  cnt = 0
  total = 0
print(res)
