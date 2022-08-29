a = [list(map(int, input().split())) for _ in range(9)]

def check(a):
  for i in range(9):
    hang = [0] * 10
    yul = [0] * 10
    for j in range(9):
      hang[a[i][j]] = 1
      yul[a[j][i]] = 1
    if sum(hang) != 9 or sum(yul) != 9:
      return False
  for k in range(3):
    for k2 in range(3):
      grp = [0] * 10
      for k3 in range(3):
        for k4 in range(3):
          grp[a[k*3+k3][k2*3+k4]] = 1
      if sum(grp) != 9:
        return False
    return True

if check(a):
  print("YES")
else:
  print("NO")
    