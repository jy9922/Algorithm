report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2

answer = [0] * len(id_list)
reports = {x:0 for x in id_list}

for i in set(report):
  reports[i.split()[1]] += 1

for i in set(report):
  if reports[i.split()[1]] >= k:
    answer[id_list.index(i.split()[0])] += 1

print(answer)
  