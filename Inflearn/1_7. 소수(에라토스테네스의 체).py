N = int(input())
cnt = 1
result = False

for i in range(3, N+1):
  for j in range(2, i):
    if i % j == 0:
      result = False
      break
    result = True
  if result == True:
    cnt += 1
    result = False

print(cnt)