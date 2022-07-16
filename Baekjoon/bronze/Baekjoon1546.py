n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
result = []

for i in score:
  new_score = i/max_score*100
  result.append(new_score)
print(round(sum(result)/n,2))