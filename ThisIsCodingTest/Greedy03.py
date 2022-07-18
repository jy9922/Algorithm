n, m = map(int, input().split())

result = 0
for i in range(n):
  card = list(map(int, input().split()))
  min_data = min(card)
  result = max(result, min_data)

print(result)
  