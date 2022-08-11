import heapq
import collections

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
K = 1

answer = []

graph = collections.defaultdict(list)
for u, v, w in flights:
  graph[u].append((v,w))

k = 0
Q = [(0, src, k)]
dist = collections.defaultdict(list)

while Q:
  time, node, k = heapq.heappop(Q)
  if node == dst:
    print(time)
    break
  if k <= K:
    k += 1
    for v, w in graph[node]:
      alt = time + w
      heapq.heappush(Q, (alt, v, k))
else:
  print(-1)
