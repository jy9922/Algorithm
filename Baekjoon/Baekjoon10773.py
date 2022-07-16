import sys
input = sys.stdin.readline

k = int(input())
stack = []

for i in range(k):
  put_in = int(input())
  if put_in == 0:
    stack.pop()
  else:
    stack.append(put_in)

print(sum(stack))
