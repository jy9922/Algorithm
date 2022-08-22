card = []
idx = 0

for i in range(1, 21):
  card.append(i)

for i in range(10):
  x, y = map(int, input().split())
  for j in range(x-1, x+(y-x)//2):
    card[j], card[y-idx-1] = card[y-idx-1], card[j]
    idx += 1
  idx = 0

print(card)


