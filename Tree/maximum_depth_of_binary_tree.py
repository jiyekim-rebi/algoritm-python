# 이진 트리의 최대 깊이
# https://leetcode.com/problems/maximum-depth-of-binary-tree
import collections
from idlelib.tree import TreeNode

class Solution:
    # 1. 반복 구조로 bfs 풀이
    # bfs: 너비 우선 탐색
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        # bfs 반복 횟수: 깊이
        return depth