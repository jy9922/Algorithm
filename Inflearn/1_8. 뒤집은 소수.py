N = int(input())
num = list(map(int, input().split()))

def reverse(x):
  x = str(x)
  x = int(x[::-1])
  result = isPrime(x)
  if result == True:
    print(x, end=" ")


def isPrime(x):
  result = True
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return result

      
for i in num:
  reverse(i)