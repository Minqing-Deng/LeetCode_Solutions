from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        max_triplet = [0, 0, 0]  # Track the max values we can achieve

        for triplet in triplets:
            # Only consider triplets that don't exceed target values
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                # Update the max values we can achieve
                max_triplet[0] = max(max_triplet[0], triplet[0])
                max_triplet[1] = max(max_triplet[1], triplet[1])
                max_triplet[2] = max(max_triplet[2], triplet[2])

        # Check if we can form the target triplet
        return max_triplet == target