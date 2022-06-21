n, m, x, y, k = map(int, input().split())
gido = []

for i in range(n):
  gido.append(list(map(int, input().split())))

order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
# 위 뒤 오 왼 앞 밑
#동서북남
def turn(dir):
  a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] 
  if dir == 1:
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
  if dir == 2:
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
  if dir == 3:
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
  if dir == 4:
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

#동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in order:
  nx += dx[i-1]
  ny += dy[i-1]

  if nx < 0 or nx >= n or ny < 0 or ny >= m:
    nx -= dx[i-1]
    ny -= dy[i-1]
    continue
  
  turn(i)
  
  if gido[nx][ny] == 0:
    gido[nx][ny] = dice[5]
  else:
    dice[5] = gido[nx][ny]
    gido[nx][ny] = 0

  print(dice[0])