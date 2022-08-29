# 행번호, 방향
n = int(input())
gam = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
order = [list(map(int, input().split())) for _ in range(m)]

result = [[] for _ in range(n)]
for i in order:
  hang, dir, num = i[0]-1, i[1], i[2]
  if dir == 0:
    num = - num
  for j in range(n):
    idx = j + num
    if idx >= n:
      idx = idx - n
    result[idx] = gam[hang][j]
  for k in range(n):
    gam[hang][k] = result[k]

res = 0
l = n // 2 - 2
r = n // 2 + 2

for i in range(n):
  
  for j in range(l, r+1):
    print(i, j)
    res += gam[i][j]
    
  if i < n // 2:
    l += 1
    r -= 1
  else:
    l -= 1
    r += 1
  
print(res)  