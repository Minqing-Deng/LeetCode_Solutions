from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(current_permutation):
            # Base case: when the current permutation contains all the numbers
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])  # Append a copy of the permutation
                return

            # Explore the decision tree by adding unused elements
            for i in range(len(nums)):
                if visited[i]:  # Skip if the number is already used
                    continue

                # Make the decision to include nums[i] in the permutation
                current_permutation.append(nums[i])
                visited[i] = True  # Mark it as visited

                # Recursive call to extend the permutation
                backtrack(current_permutation)

                # Backtrack: undo the decision, remove nums[i], and unmark visited
                current_permutation.pop()
                visited[i] = False

        result = []
        visited = [False] * len(nums)  # Track whether an element is used in the current permutation
        backtrack([])
        return result