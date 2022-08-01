from collections import deque

n, k = map(int, input().split())
answer = []
dx = [-1, 1, 2]
max_p = 10**5
visited = [0] * (max_p+1)
q = deque()
q.append(n)

while q:
  p = q.popleft()
  if p == k:
    print(visited[p])
    break
  for i in range(3):
    if i == 2:
        np = p * dx[i]
    else:
        np = p + dx[i]
    if np >= 0 and np <= max_p and visited[np] == 0:
      visited[np] = visited[p] + 1
      q.append(np)

    