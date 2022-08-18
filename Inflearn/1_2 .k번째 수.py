t = int(input())

for i in range(t):
  N, s, e, k = map(int, input().split())
  num = list(map(int, input().split()))
  
  num[s-1:e].sort()
  print("%d %d" %(i+1, num[k-1]))
  