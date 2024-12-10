from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        result = []
        p_count = Counter(p)
        s_count = Counter()

        p_length = len(p)
        for i in range(len(s)):
            # Add the current character to the window
            s_count[s[i]] += 1

            # Remove the character that goes out of the window
            if i >= p_length:
                if s_count[s[i - p_length]] == 1:
                    del s_count[s[i - p_length]]
                else:
                    s_count[s[i - p_length]] -= 1

            # Compare window and p's frequency count
            if s_count == p_count:
                result.append(i - p_length + 1)

        return result