n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
lt = 0
rt = len(a)

while lt<=rt: 
  mid = (lt + rt) // 2
  if a[mid] == m:
    print(mid+1)
    break
  elif a[mid] < m:
    lt = mid + 1
  else:
    rt = mid - 1
  
