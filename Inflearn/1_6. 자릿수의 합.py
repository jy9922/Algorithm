N = int(input())
num = list(map(int, input().split()))
result = []

def digit_sum(x):
  x_sum = 0
  for i in str(x):
    x_sum += int(i)
  return x_sum
  
max = 0

for n in num:
  a = digit_sum(n)
  if max < a:
    max = a
    res = n
print(res)
    
  
    