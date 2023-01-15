# 리스트 정렬
# https://leetcode.com/problems/sort-list/
from typing import List

from HashTable.design_hashmap import ListNode


class Solution:
    # 1. 병합 정렬
    def mergdTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergdTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # runner
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergdTwoLists(l1, l2)

    # 2. 퀵 정렬(은 불균형 리스트 문제로 구현이...)

    # 3. 내장 함수를 이용하는 방법
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head