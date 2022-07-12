tc = int(input())
result = []
answer = ''
for i in range(tc):
  n, str = input().split()
  n = int(n)
  for j in range(len(str)):
    answer += str[j]*n
  result.append(answer)
  answer = ''
for k in result:
  print(k)
  