from itertools import combinations
N, K = map(int, input().split())
card = list(map(int, input().split()))
card_sum = []

for i in combinations(card, 3):
  card_sum.append(sum(i))

card_sum.sort(reverse=True)
print(card_sum[K-1])

