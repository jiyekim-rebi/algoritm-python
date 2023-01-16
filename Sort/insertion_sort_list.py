# 삽입 정렬 리스트
# https://leetcode.com/problems/insertion-sort-list
from HashTable.design_hashmap import ListNode


class Solution:
    # head: 정렬해야 할 대상, cur: 정렬을 끝낸 대상
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            cur = parent
        return cur.next

    # 삽입 정렬의 비교 조건을 개선한 버전
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 팔요헌 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent

        return parent.next