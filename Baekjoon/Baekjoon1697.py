from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    graph[i].sort(reverse=True)

result = []
visited = [0] * (n + 1)


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

for i in range(1, n + 1):
    if i not in result:
        print(0)
    else:
        print(result.index(i) + 1)
