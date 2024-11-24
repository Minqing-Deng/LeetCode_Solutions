class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window, T = {}, {}

        for c in t:
            T[c] = T[c] + 1 if c in T else 1

        have, need = 0, len(T)

        min_length = float("inf")

        l = 0
        res = [-1, -1]

        for r in range(len(s)):

            c = s[r]

            window[c] = window[c] + 1 if c in window else 1

            if c in T and window[c] == T[c]:
                have += 1

            while have == need:
                if r - l + 1 < min_length:
                    res = [l, r]
                    min_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in T and window[s[l]] < T[s[l]]:
                    have -= 1
                l += 1

        l, r = res[0], res[1]

        return s[l:r + 1] if min_length != float("inf") else ""