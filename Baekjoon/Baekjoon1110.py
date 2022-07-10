n = input()
new_n = ''
first = n
count = 0
if int(n) < 10:
  n = '0' + n
  first = n
  
while True:
  a = str(int(n[0]) + int(n[1]))
  new_n = str(n[1]) + str(a[-1])
  count += 1
  if new_n == first:
    break
  n = new_n
    
print(count)