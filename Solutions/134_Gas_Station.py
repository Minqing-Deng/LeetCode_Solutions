from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # if the total gas is less than the total cost,
        # is impossible to finish the toute
        if sum(gas) < sum(cost):
            return -1

        currentGas = 0
        startIndex = 0

        for i in range(len(gas)):

            currentGas += (gas[i] - cost[i])

            # if the current gas is less than 0,
            # means it can not reach the next gas station
            if currentGas < 0:
                currentGas = 0
                startIndex = i + 1

        return startIndex