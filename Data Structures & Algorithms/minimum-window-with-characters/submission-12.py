class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        for c in t:
            if c not in countT:
                countT[c] = 0
            countT[c] += 1
        
        left = 0
        right = 0
        nextLeft = []
        shortest = ""
        countCopy = countT.copy()
        extras = {}
        while left < len(s) and right < len(s):       
            startL = left
            startR = right
            print("Krece sa " + str(left) + " i trazi " + str(countCopy))
            while right < len(s) and countCopy:
                if s[right] in countT and not left==right:
                    print("Nasao " + s[right] + " na " + str(right))
                    if s[right] not in countCopy:
                        if s[right] not in extras:
                            extras[s[right]] = 0
                        extras[s[right]] += 1
                    nextLeft.append(right)
                if s[right] in countCopy and not (startR==right and not left==0):
                    countCopy[s[right]] -= 1
                    if countCopy[s[right]] == 0:
                        countCopy.pop(s[right], None)
                    if not countCopy:
                        break
                right += 1

            if countCopy:
                break

            substr = s[left:right+1]
            print(str(left) + " " + str(right) + " " +  s[left:right+1] + str(countCopy))
            if len(substr) < len(shortest) or shortest == "":
                shortest = substr

            if s[left] in countT:
                if s[left] not in extras:
                    if s[left] not in countCopy:
                        countCopy[s[left]] = 0
                    countCopy[s[left]] += 1
                else:
                    extras[s[left]] -= 1
                    if extras[s[left]] <= 0:
                        extras.pop(s[left], None)


            if not nextLeft:
                break
            left = nextLeft.pop(0)
            
            
        return shortest