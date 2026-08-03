from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0

        while left < right:
            width = right - left
            area = min(heights[left], heights[right]) * width
            ans = max(ans, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans