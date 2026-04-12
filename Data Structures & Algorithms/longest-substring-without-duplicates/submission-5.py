class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        current = 0
        while current < len(s) and start < len(s):
            found = {}
            found[s[start]] = start
            current = start + 1
            while current < len(s):
                if s[current] not in found:
                    found[s[current]] = current
                    current += 1
                else:
                    break
            longest = max(longest, current-start)
            if current < len(s):
                start = found[s[current]] + 1 

        return longest