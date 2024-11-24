class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def allZero(dic):
            for key, value in dic.items():
                if value != 0:
                    return False
            return True

        if len(s1) > len(s2):
            return False
        count = {}
        for c in s1:
            count[c] = 1 + count.get(c, 0)

        tempCount = count.copy()
        l = 0
        for r in range(len(s2)):
            if s2[r] not in count:
                tempCount = count.copy()
                l = r + 1
                continue
            else:
                tempCount[s2[r]] -= 1
                if allZero(tempCount):
                    return True
                else:
                    while tempCount[s2[r]] < 0:
                        tempCount[s2[l]] += 1
                        l += 1

        return False