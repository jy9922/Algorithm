# 음료수 얼려먹기

n, m = map(int, input().split())
ice = []
count = 0

for i in range(n):
  ice.append(list(map(int, input())))

visited = []

def dfs(x, y):
  global count
  if x < 0 or x >= n or y < 0 or y >= m:
    return
  if ice[x][y] == 1:
    return
  ice[x][y] = 1
  dfs(x-1, y)
  dfs(x+1, y)
  dfs(x, y-1)
  dfs(x, y+1)
  return False

for i in range(n):
  for j in range(m):
    result = dfs(i, j)
    if result == False:
      count+=1
  
print(count)