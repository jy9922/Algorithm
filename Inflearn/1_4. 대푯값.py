N = int(input())
score = list(map(int, input().split()))
chaMin = float("inf")

score_avg = int(round(sum(score)/N,0))

for idx, x in enumerate(score):
  cha = abs(x - score_avg)
  if cha < chaMin:
    chaMin = cha
    scores = x
    res = idx + 1
  elif chaMin == cha:
    if x > scores:
      scores = x
      res = idx + 1

print(score_avg, res)
      
        
  