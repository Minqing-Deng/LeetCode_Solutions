from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            j = i + len(nums)
            output[i] = nums[i]
            output[j] = nums[i]
        return output

        # res = []
        # for i in range(2):
        #     for n in nums:
        #         res.append(n)

        # return res