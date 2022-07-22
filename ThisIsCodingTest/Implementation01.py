n = int(input())
order = list(input().split())
x, y = 1, 1

# LRUD
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
orders = ['L', 'R', 'U', 'D']

for i in order:
  j = orders.index(i)
  nx = x + dx[j]
  ny = y + dy[j]
  if nx <= 0 or ny <= 0 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(nx, ny)
  
      