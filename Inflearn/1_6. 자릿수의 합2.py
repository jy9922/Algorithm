N = int(input())
num = list(map(int, input().split()))
result = []

def digit_sum(x):
  sum = 0
  while x > 0:
    sum += x % 10
    x = x // 10
  return sum
  
max = 0

for n in num:
  a = digit_sum(n)
  if max < a:
    max = a
    res = n
print(res)
    
  