# Ư�� ���Ұ� ���� ���� ã��
def find_parent(parent, x):
  # ��Ʈ ��带 ã�� ������ ��� ȣ��
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# �� ���Ұ� ���� ������ ��ġ��
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# ����� ������ ����(Union ����)�� ���� �Է� �ޱ�
v, e = map(int, input().split())
parent = [0] * (v+1) # �θ� ���̺� �ʱ�ȭ

# �θ� ���̺� �󿡼�, �θ� �ڱ� �ڽ����� �ʱ�ȭ
for i in range(1, v+1):
  parent[i] = i

# Union ������ ���� ����
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# �� ���Ұ� ���� ���� ���
print('�� ���Ұ� ���� ����:', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()

print('�θ� ���̺�:', end='')
for i in range(1, v+1):
  print(parent[i], end=' ')