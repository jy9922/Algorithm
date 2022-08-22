import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

nn = [list(map(int, input().split())) for _ in range(n)]

hang = 0
yul = 0
nyul = 0
dagak1 = 0
dagak2 = 0

for i in range(n):
  hang = max(hang,sum(nn[i]))
  for j in range(n):
    nyul += nn[j][i]
  yul = max(yul, nyul)
  nyul = 0

for k in range(n):
  if n-k < 0:
    break
  dagak1 += nn[k][k]
  dagak2 += nn[k][n-k-1]
  dagak = max(dagak1, dagak2)
print(hang, yul, dagak)