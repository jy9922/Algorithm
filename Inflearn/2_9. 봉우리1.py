n = int(input())

san = [list(map(int, input().split())) for _ in range(1, n+1)]
res = 0
san.insert(0, [0]*n)
san.append([0]*n)

for i in san:
  i.insert(0, 0)
  i.append(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = y = 1

for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if san[i][j] <= san[nx][ny]:
        result = False
        break
      result = True
      
    if result == True:
      res += 1

print(res)