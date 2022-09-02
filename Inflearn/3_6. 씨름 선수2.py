n = int(input())
sunsu = [list(map(int, input().split())) for _ in range(n)]

print(sunsu)

sunsu.sort(reverse=True)

print(sunsu)

cnt = 1
mm = sunsu[0][1]

for k, m in sunsu[1:]:
  if mm <= m:
    cnt += 1
    mm = m
    
print(cnt)
    