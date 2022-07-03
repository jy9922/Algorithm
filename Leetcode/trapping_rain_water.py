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
  # 가장 높은 기둥이고, 높은 기둥이 하나일 때
  if left == top and height.count(top)==1:
    left = 0
  for i in range(x+1, len(height)):
    right = height[i]
    print('right', right)
    if i <= 0 or i >= len(height)-1:
      break
    # 왼쪽 기둥보다 오른쪽 기둥이 작으면 물 쌓임
    if left > right:
      water += left - right
      print('water', water)
      print()
    else:
      # 왼쪽 기둥보다 크거나 같은 기둥을 만났을 때
      q.append(height[i])
      x = i
      break

print(water)
  
  
  
