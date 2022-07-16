tc = int(input())
stu_num = []
num = 0
result = []
for i in range(tc):
  stu_num = list(map(int, input().split()))
  stu_avg = (sum(stu_num) - stu_num[0] )  / stu_num[0]
  for j in range(1, len(stu_num)):
    if stu_num[j] > stu_avg:
      num += 1
  per = num / stu_num[0] * 100
  result.append(per)
  stu_num = []
  num = 0

for i in result:
  print('{:.3f}%'.format(i))
  