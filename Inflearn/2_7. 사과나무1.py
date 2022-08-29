# 사과나무
n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
appleTree = 0

mid = n // 2 
for i in range(n):
  if i <= mid:
    for j in range(mid-i, mid+i+1):
      appleTree += tree[i][j]
      print(tree[i][j])
  else:
    print()
    for k in range(abs(mid-i), abs(mid) + (i % mid) + 1):
      appleTree += tree[i][k]
      print(tree[i][k])
    
print(appleTree)

