n = int(input())
number = list(map(int, input().split()))

stack = []
result = {}
answer = [-1] * n

stack.append(0)
for i in range(1, n):
  while stack and number[stack[-1]] < number[i]:
    answer[stack.pop()] = number[i]
  stack.append(i)

print(*answer)