# 두 이진 트리 병합
# https://leetcode.com/problems/merge-two-binary-trees
from idlelib.tree import TreeNode

class Solution:
    # 재귀 탐색
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2