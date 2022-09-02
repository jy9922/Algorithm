n = int(input())
sunsu = [list(map(int, input().split())) for _ in range(n)]

print(sunsu)

sunsu.sort(key=lambda x : (x[1], x[0]))

print(sunsu)

cnt = 0
em = 0
ek = sunsu[0][0]

for k, m in sunsu[1:]:
  if ek >= k:
    cnt += 1
    print(ek)
  ek = k
print(cnt+1)
    