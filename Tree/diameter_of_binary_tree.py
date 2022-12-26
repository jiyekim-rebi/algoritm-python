# 이진 트리의 직경
# https://leetcode.com/problems/diameter-of-binary-tree
from idlelib.tree import TreeNode


class Solution:
    # 상태값 누적 트리 dfs
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각 리프 노드까지 탐색함
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest - max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest