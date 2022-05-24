import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(n):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드를 이동하는 거리가 더 짧은 경우
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))
      
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i], end=' ')