import sys
input = sys.stdin.readline
INF = int(1e9) # ������ �ǹ��ϴ� ������ 10���� ��¡

# ����� ����, ������ ���� �Է� �ޱ�
n, m = map(int, input().split())
# ���� ��� ��ȣ �Է� �ޱ�
start = int(input())
# �� ��忡 ����Ǿ� �ִ� ��忡 ���� ������ ��� ����Ʈ �����
graph = [[] for _ in range(n+1)]
# �湮�� ���� �ִ��� üũ�ϴ� ������ ����Ʈ
visited = [False] * (n+1)
# �ִ� �Ÿ� ���̺��� ��� �������� �ʱ�ȭ
distance = [INF] * (n+1)

# ��� ���� ������ �Է¹ޱ�
for i in range(m):
  a, b, c = map(int, input().split())
  # a�� ��忡�� b������ ���� ����� c
  graph[a].append((b, c))

# �湮���� ���� ��� �߿���, ���� �ִ� �Ÿ��� ª�� ����� ��ȣ�� ��ȯ
def get_smallest_node():
  min_value = INF
  index = 0 # ���� �ִ� �Ÿ��� ª�� ���
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # ���� ��忡 ���ؼ� �ʱ�ȭ
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # ���� ��带 ������ ��ü n-1���� ��忡 ���ؼ� �ݺ�
  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    # ���� ���� ����� �ٸ� ��带 Ȯ��
    for j in graph[now]:
      cost = distance[now] + j[1]
      # ���� ��带 ���ļ� �ٸ� ���� �̵��ϴ� �Ÿ��� �� ª�� �椷
      if cost < distance[j[0]]:
        distance[j[0]] = cost

# ���ͽ�Ʈ�� �˰��� ����
dijkstra(start)

# ��� ���� ���� ���� �ִ� �Ÿ� ���
for i in range(1, n+1):
  # ������ �� ���� ���, �����̶�� ���
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i], end=' ')
      