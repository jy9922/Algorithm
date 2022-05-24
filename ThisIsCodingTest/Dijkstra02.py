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
  # ���� ���� ���� ���� �ִ� ��δ� 0���� ����, ť�� ����
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    # ���� ��尡 �̹� ó���� ���� �ִ� ����� ����
    if distance[now] < dist:
      continue
    # ���� ���� ����� �ٸ� ������ ����� Ȯ��
    for i in graph[now]:
      cost = dist + i[1]
      # ���� ��带 ���ļ�, �ٸ� ��带 �̵��ϴ� �Ÿ��� �� ª�� ���
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))
      
# ���ͽ�Ʈ�� �˰��� ����
dijkstra(start)

# ��� ���� ���� ���� �ִܰŸ� ���
for i in range(1, n+1):
  # ������ �� ���� ���, �����̶�� ���
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i], end=' ')