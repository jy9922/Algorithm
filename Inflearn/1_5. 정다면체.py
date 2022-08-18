n, m = map(int, input().split())
dice_hap = []
dice_hap2 = {}
answer = []

for i in range(1, max(n, m)+1):
  for j in range(1, min(n, m)+1):
    dice_hap.append(i+j)
    dice_hap2[i+j] = 0

for x in dice_hap:
  dice_hap2[x] += 1
  
maxVal = max(dice_hap2.values())

for x in dice_hap2:
  if dice_hap2[x] == maxVal:
    answer.append(x)

print(answer)
  