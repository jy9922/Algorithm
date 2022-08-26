n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

idx = len(a)//2 - 1

while True:
  if a[idx] == m:
    print(idx+1)
    break
  elif a[idx] < m:
    idx += 1
  else:
    idx -= 1
