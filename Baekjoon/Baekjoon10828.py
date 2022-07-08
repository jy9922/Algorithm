import sys
input = sys.stdin.readline
num = int(input())
stack = []

def push(x):
  stack.append(x)
def pop():
  if stack:
    return stack.pop()
  else:
    return -1
def size():
  return len(stack)
def empty():
  if stack:
    return 0
  else:
    return 1
def top():
  if stack:
    return stack[-1]
  else:
    return -1

for i in range(num):
  orders = input().split()
  if orders[0] == 'push':
    push(orders[1])
  elif orders[0] == 'pop':
    print(pop())
  elif orders[0] == 'size':
    print(size())
  elif orders[0] == 'empty':
    print(empty())
  else:
    print(top())
  
    
  
  