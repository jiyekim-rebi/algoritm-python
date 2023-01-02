# 정렬된 배열의 이진 탐색 트리 변환
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from idlelib.tree import TreeNode
from typing import List


class Solution:
    # 이진 검색 결과로 트리구성
    # BST: 정렬된 배열을 이진 검색으로 쪼개어 나감
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        # 정확하게 가운데값을 내림처리
        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node