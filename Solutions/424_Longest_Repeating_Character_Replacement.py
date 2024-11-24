class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window solution:

        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(count.values())
            if (r - l + 1) - maxf <= k:
                res = max(res, r - l + 1)
            else:
                while (r - l + 1) - maxf > k:
                    count[s[l]] -= 1
                    maxf = max(count.values())
                    l += 1
        return res