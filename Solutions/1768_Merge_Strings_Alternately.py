class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr1 = []
        n1 = len(word1)
        for c in word1:
            arr1.append(c)

        arr2 = []
        n2 = len(word2)
        for c in word2:
            arr2.append(c)

        i1, i2 = 0, 0
        res = []
        while i1 < n1 and i2 < n2:
            res.append(arr1[i1])
            res.append(arr2[i2])
            i1 += 1
            i2 += 1

        if i1 < n1:
            res += arr1[i1:]
        else:
            res += arr2[i2:]

        return "".join(res)