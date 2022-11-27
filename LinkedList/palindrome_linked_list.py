# 펠린드롬 연결 리스트
# https://lettcode.com/problems/palindrome-linked-list
import collections
from typing import List, Deque


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        # 펠린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    # 데크
    def isPalindrome(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # Runner 기법?
    def isPalindrome(self, head:ListNode) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해서 역순 연결 리스트를 구성함
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 펠린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev