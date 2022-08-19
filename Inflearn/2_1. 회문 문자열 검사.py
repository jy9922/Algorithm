N = int(input())
word = [input() for i in range(N)]

for i in word:
  i = i.lower()
  for j in range(len(i)//2):
    if i[j] == i[-1-j]:
      result = True
    else:
      result = False
      break
  if result == True:
    print("YES")
  else:
    print("NO")