from collections import deque

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,4],
  [1],
  [1],
  [1]
]

visited = [False] * 5
bfs(graph, 1, visited)