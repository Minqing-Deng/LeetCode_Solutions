from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack solution
        # Time: O(n)
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


        # # Brute Force solution:
        # # Time: O(n^2)
        # res = 0
        # for i, h in enumerate(heights):
        #     l = i
        #     r = i
        #     while l - 1 >= 0 and heights[l-1] >= h:
        #         l -= 1
        #     while r + 1 < len(heights) and heights[r+1] >= h:
        #         r += 1
        #     res = max(res, (r - l + 1) * h)
        # return res