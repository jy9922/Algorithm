stack = []
table = {
  ')': '(',
  ']': '['
}
while True:
  input_data = input()
  if input_data == '.':
    break
  for i in input_data:
    if i == '(' or i == '[':
      stack.append(i)
    if i == ')' or i == ']':
      if stack and stack[-1] == table[i]:
        stack.pop()
      else:
        stack.append(i)
    if i == '.':
      if len(stack) == 0:
        print('yes')
      else:
        print('no')
      stack = []    
