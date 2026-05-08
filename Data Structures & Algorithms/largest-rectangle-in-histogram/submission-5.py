class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rects = [] # Height, start
        maxArea = 0
        for i in range(len(heights)):
            #print(rects)
            current = heights[i]
            if not rects:
                rects.append((current, i))
            else:
                top = rects[-1]
                if current > top[0]:
                    rects.append((current, i))
                else:
                    while rects and current <= rects[-1][0]:
                        top = rects.pop()
                        maxArea = max(maxArea, top[0] * (i - top[1]))
                    rects.append((current, top[1]))
        #print(rects)                
        
        length = len(heights)
        for height, start in rects:
            maxArea = max(maxArea, height * (length - start))

        return maxArea

            