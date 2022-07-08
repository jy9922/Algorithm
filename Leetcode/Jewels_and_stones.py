from collections import defaultdict
j = input()
s = input()
counts = 0

table = defaultdict(list)

for i in s:
  print(i)
  if i not in table:
    table[i] = 1
  else:
    table[i] += 1

for k in j:
  if k in table:
    counts += table[k] 
print(counts)
    
  