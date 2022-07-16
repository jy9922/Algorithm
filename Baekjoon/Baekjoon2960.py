n, k = map(int, input().split())
array = [True for i in range(n+1)] #2번부터 N까지 모든 정수 적는다.
count = []
for i in range(2, n+1): #아직 지우지 않은 수 중 가장 작은 수를 찾는다.
    if array[i] == True:
      array[i] = False # P를 지우고,
      count.append(i)
      j = 2
      while i * j <= n: # 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
        if array[i*j] == True:
          array[i*j] = False
          count.append(i*j) # 지운 순서에 맞게 배열에 담는다.
        j += 1
        
print(count[k-1]) # K번째 지우는 수를 출력한다.
      