# 페어의 노드 스왑
# https://leetcode.com/problems/swap-nodes-in-pairs

class Solution:
    # 1. 그냥 값만 바꿔봄
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # 2. 반복구조로 스왑처리
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next

    # 3. 재귀로 풀자
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next

            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head