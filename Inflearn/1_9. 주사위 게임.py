N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]
answer = []

def checkMoney(dice):
  dice_count = [0] * 7
  for j in dice:
    dice_count[j] += 1
  max_count = max(dice_count)
  if max_count == 1:
    return max(dice) * 100
  if max_count == 2:
    return 1000 + dice_count.index(max_count) * 100
  if max_count == 3:
    return 10000 + dice_count.index(max_count) * 1000
      
      

for i in dice:
  result = checkMoney(i)
  answer.append(result)

print(max(answer))
    