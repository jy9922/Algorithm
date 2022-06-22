def solution(N, stages):
    answer = []
    fail = []
    fail_per = 0
    a = len(stages)
    for i in range(1, N+1):
        fail_num = stages.count(i)
        if fail_num > 0:
            fail_per = fail_num / a
        if fail_num == 0:
            fail_per = 0
        a -= fail_num
        fail.append([i, fail_per])
    
    fail.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(fail)):
        answer.append(fail[i][0])
    return answer