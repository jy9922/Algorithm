m = 4
n = 5
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
cnt = 0

def dfs(gird, x, y):
  if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == "0":
    return
  gird[x][y] = "0"
    
  dfs(grid, x+1, y)
  dfs(grid, x-1, y)
  dfs(grid, x, y-1)
  dfs(grid, x, y+1)


for i in range(m):
  for j in range(n):
    if grid[i][j] == "1":
      dfs(grid, i, j)
      cnt += 1
print(cnt)