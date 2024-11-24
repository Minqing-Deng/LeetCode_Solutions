from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Instead of True/False, store the complete word here


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Initialize the trie
        root = TrieNode()
        res = []
        visit = set()
        rows, cols = len(board), len(board[0])

        # Build Trie
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = word  # Store the word at the end node

        def dfs(r, c, node):
            if (r, c) in visit:
                return

            char = board[r][c]
            curNode = node.children.get(char)
            if not curNode:
                return

            # If we find a word, add it to the result and mark the node as visited
            if curNode.word:
                res.append(curNode.word)
                curNode.word = None  # To avoid duplicates

            visit.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            # Explore all four directions
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, curNode)

            visit.remove((r, c))

        # Start DFS for each position on the board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root)

        return res