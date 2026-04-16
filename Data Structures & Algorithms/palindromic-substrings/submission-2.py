class Solution:
    def countSubstrings(self, s: str) -> int:
        last = []
        result = 0
        substrings = {}
        for char in s:
            newLast = []
            for i in range(len(last)):
                substr = last[i]
                substr += char
                if substr not in substrings:
                    if substr == substr[::-1]:
                        substrings[substr] = True
                    else:
                        substrings[substr] = False
                if substrings[substr]:
                    result += 1
                newLast.append(substr)
            result += 1
            newLast.append(char)
            last = newLast
        return result
