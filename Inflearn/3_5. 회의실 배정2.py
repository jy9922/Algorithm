# 회의가 끝나는 시간을 기준으로 정렬!
 
n = int(input())

meet = [list(map(int, input().split())) for _ in range(n)]

print(meet)

meet.sort(key=lambda x: (x[1],x[0]))

et = 0
cnt = 0
for s, e in meet:
  if s >= et:
    et = e
    cnt += 1

print(cnt)