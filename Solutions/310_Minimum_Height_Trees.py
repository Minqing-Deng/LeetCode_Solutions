from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        # Build the graph as an adjacency list
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Initialize leaves (nodes with only one connection)
        leaves = deque(node for node in range(n) if len(graph[node]) == 1)

        # Trim the tree level by level
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # The only neighbor of a leaf
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                # If the neighbor becomes a leaf, add it to the queue
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        # The remaining nodes are the roots of MHTs
        return list(leaves)