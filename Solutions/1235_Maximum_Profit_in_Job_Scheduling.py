from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        endTimes = [job[1] for job in jobs]

        dp = [0] * len(jobs)

        for i in range(len(jobs)):
            current_profit = jobs[i][2]

            j = bisect_right(endTimes, jobs[i][0]) - 1 # the last non-overlapping job
            if j >= 0:
                current_profit += dp[j]

            dp[i] = max(dp[i-1] if i-1 >= 0 else 0, current_profit)

        return dp[-1]