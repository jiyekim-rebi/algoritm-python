# 균형 이진 트리
# https://leetcode.com/problems/balanced-binary-tree
from idlelib.tree import TreeNode

class Solution:
    # 재귀 구조로 높이 차이 계산
    # 높이 균형을 매번 맞추는 AVL 트리
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)

            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(root) != -1