import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6);
n, m, r = map(int, input().split())
V = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
  u, v = map(int, input().split())
  V[u].append(v)
  V[v].append(u)
for j in V:
  j.sort(reverse=True)

cnt = 0
def dfs(V, r):
  global cnt
  if visited[r] != 0:
    return
  visited[r] = cnt + 1
  cnt += 1
  for idx in V[r]:
    dfs(V, idx)
dfs(V, r)

for i in range(1, len(visited)):
  print(visited[i])
  
  
  