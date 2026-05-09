class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = {}
        cantBeJudge = set()
        foundJudge = -1
        for person, trustedPerson in trust:
            cantBeJudge.add(person)
            if trustedPerson not in trusting:
                trusting[trustedPerson] = set()
            trusting[trustedPerson].add(person)
            if len(trusting[trustedPerson]) == n - 1 and trustedPerson not in trusting[trustedPerson] and trustedPerson not in cantBeJudge:
                if foundJudge == -1:
                    foundJudge = trustedPerson
                else:
                    return -1
            if len(trusting[trustedPerson]) == n and foundJudge == trustedPerson:
                foundJudge = -1
            if foundJudge == person:
                foundJudge = -1
        return foundJudge