n = int(input())
su = list(map(int, input().split()))
sun = [0] * n

for i in range(n):
  for j in range(n):
    if su[i] == 0 and sun[j] == 0:
      sun[j] = i + 1
      break
    elif sun[j] == 0:
      su[i] -= 1
for x in su:
  print(x, end=' ')
      
  
