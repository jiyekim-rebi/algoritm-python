# 역순 연결 리스트 2
# https://reetcode.com/problems/reverse-linked-list-ii

class Solution:
    # 반복 구조로 노드 뒤집기
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 예외 처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 뒤집기
        for _ in range(n - m):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next