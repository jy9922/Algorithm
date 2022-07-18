money = int(input())
re_money = 1000 - money
count = 0
coin = [500, 100, 50, 10, 5, 1]

for i in coin:
  if i <= re_money:
    count += re_money // i
    re_money %= i
print(count)