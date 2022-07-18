n = int(input())
distance = list(map(int, input().split()))
juyou = list(map(int, input().split()))

total = sum(distance)
result = 0
min_pay = max(juyou)

for i in range(len(distance)):
  min_pay = min(min_pay, juyou[i])
  result += distance[i] * min_pay

print(result)
