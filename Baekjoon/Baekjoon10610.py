n = list(input())
n.sort(reverse=True)
arr = list(map(int, n))

b = sum(arr)
if b % 3 == 0:
  arr.sort(reverse=True)
  if arr[-1] != 0:
    print(-1)
  else:
    a = ''.join(map(str,arr))
    a = int(a)
    print(a)
else:
  print(-1)
