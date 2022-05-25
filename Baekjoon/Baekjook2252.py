from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
result = []

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

def line_student():
  global result
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

line_student()

for i in result:
  print(i, end = ' ')