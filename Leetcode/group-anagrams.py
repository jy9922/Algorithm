import collections
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagrams = collections.defaultdict(list)
    
      for i in strs:
        a = ''.join(sorted(i))
        anagrams[a].append(i)
        
      return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]
a = Solution()
print(a.groupAnagrams(strs))