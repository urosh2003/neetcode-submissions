class Solution:
    def longestPalindrome(self, s: str) -> str:
        last = []
        result = s[0]
        substrings = set()
        for char in s:
            newLast = []
            for i in range(len(last)):
                substr = last[i]
                substr += char
                if substr not in substrings:
                    if substr == substr[::-1] and len(substr) > len(result):
                        result = substr
                    substrings.add(substr)
                newLast.append(substr)
            newLast.append(char)
            last = newLast
        return result
