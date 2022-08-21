from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())

chonsu = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
  x, y = map(int, input().split())
  chonsu[x].append(y)
  chonsu[y].append(x)

q = deque()
q.append((start, 0))

while q:
  p, cnt = q.popleft()
  if p == end:
    print(cnt)
    break
  if visited[p] == 0:
    visited[p] = 1
    cnt += 1
    for i in chonsu[p]:
      q.append((i, cnt))
else:
  print(-1)
