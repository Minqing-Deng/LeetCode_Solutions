from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["cat", "day", "atc", "ayd", "tca"]
        # output: [["cat", "atc", "tca"], ["day", "ayd"]]

        # the input only contains lower case English letters

        # the number of letters is 26: list = [0, 0, 0, ..., 0] 26 elements of
        # a list to store the presence of a letter

        anagram_list = defaultdict(list) # {[1, 0, 1, ..., 1]: "cat", "atc"} to represent "cat"

        for s in strs:
            count = [0] * 26 # [0, 0, ..., 0] 26 elements of 0
            for c in s:
                # forexample: a in index of 0, b in index of 1, ....
                # if the ascii of a is 80, and then the ascii of b would be 81
                # if we want to get the index of b, which is 1 in our count list,
                count[ord(c) - ord("a")] = count[ord(c) - ord("a")] + 1

            anagram_list[tuple(count)].append(s)

        return anagram_list.values()
