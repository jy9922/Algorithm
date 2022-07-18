from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(input()))
  
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'R':
      rx, ry = i, j
    elif graph[i][j] == 'B':
      bx, by = i, j
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
  q = deque()
  q.append((rx, ry, bx, by))
  visited = []
  visited.append((rx, ry, bx, by))
  count = 0
  while q:
    for _ in range(len(q)):
      print(q)
      rx, ry, bx, by = q.popleft()
      if count > 10:
        print(-1)
        return
      if graph[rx][ry] == 'O':
        print(count)
        return
      for i in range(4): # 4가지 방향 탐색
        nrx, nry = rx, ry
        while True:
          nrx += dx[i]
          nry += dy[i]
          if graph[nrx][nry] == '#':
            nrx -= dx[i]
            nry -= dy[i]
            break
          if graph[nrx][nry] == 'O':
            break
        nbx, nby = bx, by
        while True:
          nbx += dx[i]
          nby += dy[i]
          if graph[nbx][nby] == '#':
            nbx -= dx[i]
            nby -= dy[i]
            break
          if graph[nbx][nby] == 'O':
            break
        if graph[nbx][nby] == 'O':
          continue
          
        if nrx == nbx and nry == nby: #구슬의 위치가 같다면,
          if abs(nrx-rx)+abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
            
        if (nrx, nry, nbx, nby) not in visited:
          q.append((nrx, nry, nbx, nby))
          visited.append((nrx, nry, nbx, nby))
    count += 1
    print(count)
  print(-1)
  
bfs(rx, ry, bx, by) // 정답
      
          
          
            
        