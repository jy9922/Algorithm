n, m = map(int, input().split())
kg = list(map(int, input().split()))

kg.sort()
print(kg)
l_kg = 0
r_kg = n-1
cnt = 0
res = 0

while l_kg <= r_kg:
  if kg[l_kg] + kg[r_kg] > m:
    res += 1
    r_kg -= 1
  else:
    cnt += 1
    l_kg += 1
    r_kg -= 1
  
print(cnt+res)