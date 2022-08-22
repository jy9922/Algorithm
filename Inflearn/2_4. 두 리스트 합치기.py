n = int(input())
nNum = list(map(int, input().split()))
n2 = int(input())
n2Num = list(map(int, input().split()))

newNum = nNum + n2Num
newNum.sort()
print(newNum)