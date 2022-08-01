<<<<<<< HEAD
=======
from collections import defaultdict
>>>>>>> 0ebe24aca0cc9e59ee493e85228ecb5bd2ebb8b7
from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
<<<<<<< HEAD
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort(reverse=True)
    #내림차순


def bfs(graph, start):
    cnt = 1
    q = deque()
    q.append(start)
    visited[start] = cnt
    cnt += 1
    while q:
        new = q.popleft()
        for k in graph[new]:
            if visited[k] == 0:
                q.append(k)
                visited[k] = cnt
                cnt += 1


bfs(graph, r)
for i in visited[1::]:
    print(i)
=======
graph = defaultdict(list)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in graph:
  graph[i].sort(reverse=True)

result = []
visited = [0] * (n+1)

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    result.append(v)
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

bfs(graph, r, visited)

for i in range(1, n+1):
  if i not in result:
    print(0)
  else:
    print(result.index(i) +1)
>>>>>>> 0ebe24aca0cc9e59ee493e85228ecb5bd2ebb8b7
