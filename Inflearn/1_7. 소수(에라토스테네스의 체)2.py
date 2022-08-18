N = int(input())
cnt = [0] * (N+1)
cntt = 0

for i in range(2, N+1):
  if cnt[i] == 0:
    cntt += 1
    for j in range(i, N+1, i):
      cnt[j] = 1

print(cntt)