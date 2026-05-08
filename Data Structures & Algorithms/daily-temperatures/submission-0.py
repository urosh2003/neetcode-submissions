class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            nextBigger = i
            while stack:
                temp = temperatures[i]
                top = stack.pop()
                if temp < temperatures[top]:
                    stack.append(top)
                    nextBigger = top
                    break

            stack.append(i)
            result[i] = nextBigger - i

        return result