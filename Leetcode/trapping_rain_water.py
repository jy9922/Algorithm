from collections import deque
height = [4,2,3]

top = max(height)
q = deque()
q.append(height[0])
x = 0

water = 0
while q:
  print(q)
  left = q.popleft()
  print('left', left)
  # ���� ���� ����̰�, ���� ����� �ϳ��� ��
  if left == top and height.count(top)==1:
    left = 0
  for i in range(x+1, len(height)):
    right = height[i]
    print('right', right)
    if i <= 0 or i >= len(height)-1:
      break
    # ���� ��պ��� ������ ����� ������ �� ����
    if left > right:
      water += left - right
      print('water', water)
      print()
    else:
      # ���� ��պ��� ũ�ų� ���� ����� ������ ��
      q.append(height[i])
      x = i
      break

print(water)
  
  
  
