t =  [73,74,75,71,69,72,76,73]

stack = []
result = [0] * len(t)

for i, curr in enumerate(t):
  while stack and curr > t[stack[-1]]:
    last = stack.pop()
    result[last] = i - last
  stack.append(i)

print(result)