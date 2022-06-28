def solution(s):
    answer = 1000
    for n in range(1, len(s)+1):
        sen= ''
        cnt = 1
        tmp = s[:n]
        for i in range(n, len(s)+n, n):
            if tmp == s[i:i+n]:
                cnt += 1
            else:
                if cnt == 1:
                    sen += tmp
                else:
                    sen += str(cnt)+tmp
                tmp = s[i:i+n]
                cnt = 1
        answer = min(answer, len(sen))
    return answer