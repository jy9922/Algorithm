N = int(input())
answer = list(map(int, input().split()))
score = 0
total = 0

for i in answer:
  if i == 1:
    score += 1
    total += score
  if i == 0:
    score = 0
print(total)