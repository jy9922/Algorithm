n, k = map(int, input().split())
array = [True for i in range(n+1)] #2������ N���� ��� ���� ���´�.
count = []
for i in range(2, n+1): #���� ������ ���� �� �� ���� ���� ���� ã�´�.
    if array[i] == True:
      array[i] = False # P�� �����,
      count.append(i)
      j = 2
      while i * j <= n: # ���� ������ ���� P�� ����� ũ�� ������� �����.
        if array[i*j] == True:
          array[i*j] = False
          count.append(i*j) # ���� ������ �°� �迭�� ��´�.
        j += 1
        
print(count[k-1]) # K��° ����� ���� ����Ѵ�.
      