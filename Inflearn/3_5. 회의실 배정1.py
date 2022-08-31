n = int(input())

meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: x[0])
cnt = 0
res = 0

for i in range(n):
  pre = meeting[i][1]
  for j in range(i, n):
    if pre <= meeting[j][0]:
      res += 1
  cnt = max(cnt, res)
  res = 0
print(cnt)
