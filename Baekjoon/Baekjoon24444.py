from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort(reverse=True)
    #오름차순

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
