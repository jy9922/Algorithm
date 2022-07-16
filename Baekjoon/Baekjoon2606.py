n = int(input())
m = int(input())

computer = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int, input().split())
  computer[x].append(y)
  computer[y].append(x)

visited = [0]*(n+1)

def dfs(computer, idx):
  if visited[idx] != 0:
    return
  visited[idx] = 1
  if computer[idx] == []:
    return
  for i in computer[idx]:
    dfs(computer, i)

dfs(computer, 1)
print(visited.count(1) - 1)
  
  
  