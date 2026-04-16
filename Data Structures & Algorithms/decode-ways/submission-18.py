class Solution:

    """
    10 1 2
    10 12

    3
    """
    def numDecodings(self, s: str) -> int:
        last = [0,0,0] 
        ways = 0
        lastlast = 0
        for i in range(len(s)):
            current = [0, 0, 0]
            if i > 0:
                if s[i] == '0':
                    if last[2] > 2 or last[2] == 0:
                        return 0
                    current[1] = last[0]
                    current[0] = 0
                else:
                    if last[2] > 0 and last[2] <=2:
                        if int(s[i]) <= 6:
                            current[1] = last[0]
                            current[0] = last[1] + last[0]
                        else:
                            current[1] = 0
                            current[0] = last[1] + last[0]
                    else: # 3 
                        current[1] = 0
                        current[0] = last[1] + last[0]
            else:
                if s[i] == '0':
                    return 0
                current = [1, 0, s[i]]
            current[2] = int(s[i])

            if s[i] == '0':
                ways = max(lastlast * (current[0] + current[1]), 1)
            else:
                ways = max(ways, current[0] + current[1])

            lastlast = last[0] + last[1]
            last = current

            

            print(last)

        return ways