from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dp = {}
        # wordSet = set(dictionary)
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)

        def dfs(i):
            if i == len(s):
                return 0

            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # skip the current character

            # use Tries data structure to check if the word in the dictionary or not
            cur = trie.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.isWord:
                    res = min(res, dfs(j + 1))

            # for j in range(i, len(s)):
            #     if s[i:j+1] in wordSet:
            #         res = min(res, dfs(j+1))

            dp[i] = res
            return res

        return dfs(0)