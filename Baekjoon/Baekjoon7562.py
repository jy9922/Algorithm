from collections import deque
tc = int(input())

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

for i in range(tc):
  
  n = int(input())
  x, y = map(int, input().split())
  px, py = map(int, input().split())

  graph = [[0] * n for _ in range(n)]
  q = deque()
  q.append((x, y))
  
  while q:
    x, y = q.popleft()
    if x == px and y == py:
      print(graph[x][y])
      break
    for j in range(8):
      nx = x + dx[j]
      ny = y + dy[j]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
