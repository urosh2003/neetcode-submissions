class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        length = len(s)
        start = 0
        current = 0
        currentChar = ""

        while start < length and current < length:
            availableSwaps = k
            nextStart = start
            current = start + 1
            while current < length:
                if s[current] != s[start]:
                    if availableSwaps == k:
                        nextStart = current
                    if availableSwaps == 0:
                        break
                    availableSwaps -= 1
                    
                current += 1
            longest = max(longest, current - start)
            if start == length - 1 or k == 0 or s[start] == s[start+1]:
                start = nextStart
                continue

            availableSwaps = k - 1
            current = start + 1
            nextToStart = s[start+1]
            while current < length:
                if s[current] != nextToStart:
                    if availableSwaps == 0:
                        break
                    availableSwaps -= 1
                current += 1
            longest = max(longest, current - start)
            start = nextStart

        start = length - 1
        current = length - 1

        while start > -1 and current > -1:
            availableSwaps = k
            nextStart = start
            current = start - 1
            while current > -1:
                if s[current] != s[start]:
                    if availableSwaps == k:
                        nextStart = current
                    if availableSwaps == 0:
                        break
                    availableSwaps -= 1
                    
                current -= 1
            longest = max(longest, start - current)
            if start == 0 or k == 0 or s[start] == s[start-1]:
                start = nextStart
                continue

            availableSwaps = k - 1
            current = start - 1
            nextToStart = s[start-1]
            while current < length:
                if s[current] != nextToStart:
                    if availableSwaps == 0:
                        break
                    availableSwaps -= 1
                current -= 1
            longest = max(longest, start - current)
            start = nextStart


        return longest

        """
        while start > -1 and current > -1:
            availableSwaps = k
            nextStart = start
            current = start - 1
            while current > - 1:
                if s[current] != s[start]:
                    if availableSwaps == k:
                        nextStart = current
                    if availableSwaps == 0:
                        break
                    availableSwaps -= 1
                    
                current -= 1
            longest = max(longest, start - current)
            start = nextStart
        """
