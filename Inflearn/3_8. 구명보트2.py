from collections import deque

n, m = map(int, input().split())
kg = list(map(int, input().split()))

kg.sort()
kg = deque(kg)
cnt = 0

while kg:
  if len(kg) == 1:
    cnt += 1
    break
  if kg[0]+kg[-1] > m:
    kg.pop()
    cnt += 1
  else:
    kg.popleft()
    kg.pop()
    cnt += 1
    
print(cnt)