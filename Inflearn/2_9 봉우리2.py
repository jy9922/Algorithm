n = int(input())

san = [list(map(int, input().split())) for _ in range(1, n+1)]
res = 0
san.insert(0, [0]*n)
san.append([0]*n)
for i in san:
  i.insert(0, 0)
  i.append(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = y = 1

for i in range(1, n+1):
  for j in range(1, n+1):
    if all(san[i][j] > san[i+dx[k]][j+dy[k]] for k in range(4)):
      res += 1
print(res)

# all() - 안에 있는 조건이 모두 참일 때 조건을 만족하는 함수
      