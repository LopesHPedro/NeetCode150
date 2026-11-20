from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            countS = Counter(s)
            countT = Counter(t)
            
            return countT == countS