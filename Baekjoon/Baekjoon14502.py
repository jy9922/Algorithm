from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

cost_box = [0]

def bfs(day, cost):
  q = deque()
  q.append((day, cost))
  pay = cost
  while q:
    days, cost = q.popleft()
    x = days + graph[days-1][0]
    
    if x <= n+1:
      cost_box.append(pay)
      for i in range(x, n+1):
        if i + graph[i-1][0] > n+1:
          continue
        else:
          cost_box.append(pay)
          pay = cost + graph[i-1][1]
          q.append((i, pay))
          cost_box.append(pay)

for i in range(1, n+1):
  bfs(i, graph[i-1][1])

print(max(cost_box))