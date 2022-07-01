from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        log_num = []
        log_lets = []

        for i in logs:
            if i.split()[1].isdigit():
                log_num.append(i)
            else:
                log_lets.append(i)

        log_lets = sorted(log_lets, key= lambda x: (x.split()[1:],x.split()[0]))
        return log_lets + log_num

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
a = Solution()
print(a.reorderLogFiles(logs))