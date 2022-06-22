import re
def solution(s):
    s = re.sub('one','1',s)
    s = re.sub('two','2',s)
    s = re.sub('three','3',s)
    s = re.sub('four','4',s)
    s = re.sub('five','5',s)
    s = re.sub('six','6',s)
    s = re.sub('seven','7',s)
    s = re.sub('eight','8',s)
    s = re.sub('nine','9',s)
    s = re.sub('zero','0',s)
    answer = int(s)
    return answer