s = list(input())
stack = []
cnt = 0

for i in range(len(s)):
  if s[i] == '(':
    stack.append(s[i])
  elif s[i] == ')':
    if s[i-1] == '(':
      stack.pop()
      cnt += len(stack)
    elif s[i-1] == ')':
      stack.pop()
      cnt += 1
  
print(cnt)
