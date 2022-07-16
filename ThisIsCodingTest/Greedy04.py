n, k = map(int, input().split())
count = 0

if n % k != 0:
  while True:
    if n % k == 0:
      break
    n = n - 1
    count += 1

while True:
  n = n // k
  count += 1
  if n == 1:
    break
    
print(count)