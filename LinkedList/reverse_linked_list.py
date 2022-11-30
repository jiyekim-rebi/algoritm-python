# 역순 연결 리스트
# https://leetcode.com/ploblems/reverse-linked-list

class Solution:
    # 재귀 구조
    def reverseList(self, head:ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    # 반복 구조
    def reverseList(self, head:ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev