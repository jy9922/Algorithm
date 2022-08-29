# 행번호, 방향
n = int(input())
gam = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
  h, t, k = map(int, input().split())
  if t == 0:
    for _ in range(k):
      gam[h-1].append(gam[h-1].pop(0))
  else:
    for _ in range(k):
      gam[h-1].insert(0, gam[h-1].pop())
      
res = 0
l = 0
r = n-1

for i in range(n):
  
  for j in range(l, r+1):
    res += gam[i][j]
    
  if i < n // 2:
    l += 1
    r -= 1
  else:
    l -= 1
    r += 1
  
print(res)  