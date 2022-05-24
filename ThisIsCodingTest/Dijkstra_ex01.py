import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드와 간선 그리고 시작값 입력
n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
dijkstra(c)

count = 0
result = []
for i in range(1, n+1):
  if distance[i] != INF:
    result.append(distance[i])
    count += 1

print(count-1)
print(max(result))
  
  