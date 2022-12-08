# 두 수의 덧셈
# https://leetcode.com/problems/add-two-numbers
from typing import List

class Solution:
    # 1. 자료형으로 변환해서 풀어보면?
    # 역순으로 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node.next

        return prev

    # 연결리스트를 파이썬 리스트로 변환처리
    def toList(self, node:ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 노드를 반복하며 값을 리스트에 추가하는 함수
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 더합시다
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        # str로 각 항목을 문자로 변경한 다음 join으로 합쳤음 -> 더하기 위해 int형으로 변경
        # resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))
        # functools.reduce lambda
        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))

    # =================================================
    # 2. 전가산기 구현: Full Adder
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                l1 = l1.next
                sum += l1.val
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫과 나머지 계산
            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next