n, m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)
first = num[0]
second = num[1]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += first * count
result += (m-count) * second

print(result)