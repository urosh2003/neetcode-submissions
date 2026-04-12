class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(left, right):
            lheight = heights[left]
            rheight = heights[right]
            area = min(lheight, rheight) * (right - left)
            return area
        maxx = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            lheight = heights[left]
            rheight = heights[right]
            print("====")
            print(lheight)
            print(rheight)
            print(left)
            print(right)
            print("====")
            area = calcArea(left,right)
            if area > maxx:
                maxx = area
            
            if left >= len(heights) - 1 or right <= 0:
                break


            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxx