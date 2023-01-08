# 이진 탐색 트리(BST) 노드 간 최소 거리
# https://leetcode.com/problems/minimum-distance-between-bst-nodes
import sys
from idlelib.tree import TreeNode

class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 1. 재귀 구조로 중위 순회
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


    # 2. 반복 구조로 중위 순회
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result