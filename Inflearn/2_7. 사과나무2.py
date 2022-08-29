n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
appleTree = 0
l = r = n//2

for i in range(n):
    for j in range(l, r+1):
      appleTree+=tree[i][j]
    if i < n//2:
      l -= 1
      r += 1
    else:
      l += 1
      r -= 1
    
print(appleTree)