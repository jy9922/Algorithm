sen = input()
res = ''
for i in sen:
  if i.isnumeric():
    res += i
    
cnt = 0
res = int(res)

for i in range(1,res+1):
  if res % i == 0:
    cnt += 1
print(res)
print(cnt)
