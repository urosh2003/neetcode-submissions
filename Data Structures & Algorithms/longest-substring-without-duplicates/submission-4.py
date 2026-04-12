class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        current = 0
        while current < len(s) and start < len(s):
            found = set()
            found.add(s[start])
            current = start + 1
            while current < len(s):
                if s[current] not in found:
                    found.add(s[current])
                    current += 1
                else:
                    break
            longest = max(longest, current-start)
            while current < len(s) and s[current] != s[start] and start < len(s) - 1:
                start += 1
            start += 1

        return longest