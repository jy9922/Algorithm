from collections import defaultdict
str = " "

str_leng = 0
table = defaultdict(list)

if len(str) == 1:
  print(1)
  
for i in range(len(str)):
  table[str[i]] = 1
  for j in str[i+1:]:
    if j not in table:
      table[j] = 1
    elif j in table:
      break
  str_leng = max(str_leng, len(table.keys()))
  table = defaultdict(list)
  
print(str_leng)

  
      
      
      
  