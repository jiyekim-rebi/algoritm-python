# 전위, 중위 순회 결과로 이진 트리 구축
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))  # 시간 복잡도 O(n)

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder.pop(0))
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node