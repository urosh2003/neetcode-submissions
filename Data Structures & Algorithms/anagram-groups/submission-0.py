class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmaps = []

        for string in strs:
            strmap = [0]*26
            for i in range(len(string)):
                strmap[ord(string[i]) - ord('a')] += 1
            strmaps.append(strmap)

        groups = []
        for i in range(len(strs)):
            string = strmaps[i]
            inserted = False
            for group in groups:
                smap = group[0][0]
                if smap == string:
                    group.append((string, i))
                    inserted = True
                    break
            if not inserted:
                groups.append([(string, i)])
        
        result = []
        for group in groups:
            out = []
            for lis, i in group:
                out.append(strs[i])
            result.append(out)
        return result
            
