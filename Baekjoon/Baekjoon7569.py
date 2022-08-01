from collections import deque
import sys
input = sys.stdin.readline

q = deque()
m, n, h = map(int, input().split())
graph = []
for i in range(h):
  tmp = []
  for j in range(n):
    tmp.append(list(map(int, input().split())))
    for k in range(m):
      if tmp[j][k] == 1:
        q.append((i, j, k))   
  graph.append(tmp)


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while q:
  x, y, z = q.popleft()
  
  for i in range(6):
    nx = x + dx[i] #h
    ny = y + dy[i] #x
    nz = z + dz[i] #y

    if 0<=nx< h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
      graph[nx][ny][nz] = graph[x][y][z] + 1
      q.append((nx,ny,nz))

day = 0
for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    day = max(day, max(j))
print(day-1)