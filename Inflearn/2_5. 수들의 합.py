n, m = map(int, input().split())

nNum = list(map(int, input().split()))
cnt = 0

for i in range(n):
  for j in range(i+1, n+1):
    if sum(nNum[i:j]) == m:
      cnt += 1
print(cnt)