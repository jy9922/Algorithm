# �ּ� ��
import heapq

# �������� �� ����(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # ��� ���Ҹ� ���ʴ�� ���� ����
  for value in iterable:
    heapq.heappush(h, value)
  # ���� ���Ե� ��� ���Ҹ� ���ʴ�� ������ ���
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# �ִ� ��
import heapq

# �������� �� ����(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # ��� ���Ҹ� ���ʴ�� ���� ����
  for value in iterable:
    heapq.heappush(h, -value)
  # ���� ���Ե� ��� ���Ҹ� ���ʴ�� ������ ���
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
