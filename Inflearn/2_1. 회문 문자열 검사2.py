N = int(input())
word = [input() for i in range(N)]

for i in word:
  i = i.lower()
  if i == i[::-1]:
    print("YES")
  else:
    print("NO")
    