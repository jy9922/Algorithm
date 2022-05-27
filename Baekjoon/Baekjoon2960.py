n, k = map(int, input().split())
array = [True for i in range(n+1)]
count = []
for i in range(2, n+1):
    if array[i] == True:
      array[i] = False
      count.append(i)
      j = 2
      while i * j <= n:
        if array[i*j] == True:
          array[i*j] = False
          count.append(i*j)
        j += 1
        
print(count[k-1])
      