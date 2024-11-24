class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if not magazine:
            return False
        if len(ransomNote) > len(magazine):
            return False

        maga_count = {}
        for c in magazine:
            maga_count[c] = maga_count[c] + 1 if c in maga_count else 1

        for c in ransomNote:
            if c not in maga_count or maga_count[c] == 0:
                return False
            else:
                maga_count[c] -= 1

        return True