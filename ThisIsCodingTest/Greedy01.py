n = int(input())
coin = [500,100,50,10]
count = 0

for i in coin:
  count += n // i
  n = n % i

print(count)