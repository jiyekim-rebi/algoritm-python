# 이진 트리 반전
# https://leetcode.com/problems/invert-binary-tree
import collections
from idlelib.tree import TreeNode

class Solution:
    # 파이썬 답게 풀어보면
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        # 생략 가능
        return None

    # 반복 구조로 bfs
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()  # 처음값 추출
            # 부모 노드부터 하향식으로 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    # 반복 구조로 dfs
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()  # 마지막값 추출
            # 부모 노드부터 하향식으로 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root

    # 반복 구조로 dfs 후위 순회
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()  # 마지막값 추출

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left # 후위 순회

        return root