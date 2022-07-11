namer = []
for i in range(10):
  number = int(input())
  namer.append(number%42)
namer = set(namer)
print(len(namer))

