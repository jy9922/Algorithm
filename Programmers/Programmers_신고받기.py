def solution(id_list, report, k):
    n =  len(id_list)

    id_list_num = {} # id�� �ε��� �ο�
    new_report = set(report) #�ߺ� ����
    new_group = [[] for _ in range(n+1)] # ���� ���� ���� �迭
    counting = {} # �Ű� ���� �� ����
    final = [] # k�� �̻� �Ű� ���� ��� ����Ʈ

    answer = [0] * n

    j = 0
    for i in id_list:
        j += 1
        id_list_num.setdefault(i, j)
        counting.setdefault(i, 0)

    for j in new_report:
        a, b = j.split()
        counting[b] += 1
        for i in id_list_num:
            if a == i:
                num = id_list_num[i]
                new_group[num].append(b)
    for i in counting:
        if counting[i] >= k:
            final.append(i)
    num = 0
    for i in range(1, n+1):
        for j in final:
            if j in new_group[i]:
                num += 1
        answer[i-1] = num
        num = 0

    return answer
