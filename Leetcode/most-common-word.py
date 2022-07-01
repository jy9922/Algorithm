import re
from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        paragraph = re.sub('[^A-Za-z0-9 ]',' ', paragraph)
        a = list(paragraph.split())

        li = [i for i in a if i not in banned]
        d = Counter(li)
        result = [k for k,v in d.items() if max(d.values()) == v]
        
        return result[0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
a = Solution()
print(a.mostCommonWord(paragraph, banned))