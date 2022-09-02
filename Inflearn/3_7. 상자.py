n = int(input())
sang = list(map(int, input().split()))
m = int(input())

for i in range(m):
  larg = sang.index(max(sang))
  lowg = sang.index(min(sang))
  sang[larg] -= 1
  sang[lowg] += 1

print(max(sang)-min(sang))