n = int(input())
result = list()
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse = True)

result = [a[i] * b[i] for i in range(len(b))]

print(sum(result))