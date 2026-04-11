class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first = {}
        for c in s:
            if c not in first:
                first[c] = 0
            first[c] += 1
        for c in t:
            if c not in first or first[c] == 0:
                return False
            else:
                first[c] -= 1
                
        return True