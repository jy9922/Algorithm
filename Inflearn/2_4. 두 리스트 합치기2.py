# sort()를 이용하지 않고 문제 풀기
# O(n) 으로 해결 가능!

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

c = []

p1, p2 = 0, 0
while p1<n and p2<m:
  if nlist[p1] < mlist[p2]:
    c.append(nlist[p1])
    p1 += 1
  else:
    c.append(mlist[p2])
    p2 += 1

if p1 < n:
  c += nlist[p1:]
else:
  c += mlist[p2:]
  
for x in c:
  print(x, end=' ')