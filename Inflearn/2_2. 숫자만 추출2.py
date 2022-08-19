sen = input()
res = 0
for x in sen:
  # isdigit() 알파벳이 아닌 숫자 형태를 다 찾아주는 함수
  # isdecimal() 0-9 까지의 숫자
  if x.isdecimal():
    res = res * 10 + int(x)
print(res) 
cnt = 0
for i in range(1, res+1):
  if res % i == 0:
    cnt += 1
print(cnt)