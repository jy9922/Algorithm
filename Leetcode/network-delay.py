import collections
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

graph = collections.defaultdict(list)

for u, v, w in times:
  graph[u].append((v,w))

Q = [(0, k)]
dist = collections.defaultdict(int)

while Q:
  time, node = heapq.heappop(Q)
  if node not in dist:
    dist[node] = time
    for v, w in graph[node]:
      alt = time + w
      heapq.heappush(Q, (alt, v))

if len(dist) == n:
  print(max(dist.values()))
else:
  print(-1)

  