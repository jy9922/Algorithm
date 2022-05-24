import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijkstra(start, distance):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
        continue
    for j in graph[now]:
      cost = dist + j[1]
      if distance[j[0]] > cost:
        distance[j[0]] = cost
        heapq.heappush(q, (cost, j[0]))

x, k = map(int, input().split())
dijkstra(1, distance)
# È¸»ç(1) -> K -> X
result = 0
result += distance[k]

distance = [INF] * (n+1)
dijkstra(k, distance)
result += distance[x]

print(result)
  