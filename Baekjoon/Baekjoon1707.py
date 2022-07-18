import sys
from collections import defaultdict

tc = int(sys.stdin.readline())
graph = defaultdict(list)
answer = []

def dfs(k, group): 
  visited[k] = group
  for i in graph[k]:
    if not visited[i]:
      dfs(i, -group)
      return False
    elif visited[k] == visited[i]:
      return False
    
  return True
     
for i in range(tc):
  V, e = map(int, sys.stdin.readline().split())
  visited = [False] * (V+1)
  for j in range(e):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
  for k in graph:
    if not visited[k]:
      result = dfs(k, 1)
  if result == True:
    answer.append("YES")
  else:
    answer.append("NO")
for i in answer:
  print(i)
    