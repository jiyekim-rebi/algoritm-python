# 이진탐색트리를 더 큰수 합계 트리로
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
from idlelib.tree import TreeNode


# 자신보다 더 큰 값을 가진 모든 노드의 합
class Solution:
    # 중위 순회로 노드 값 누적
    # BST의 우측 자식 노드는 항상 부모 노드보다 큰 값임
    # 오른쪽-부모-왼쪽 순으로 전개됨
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root