# 원점에 k번째로 가까운 점
# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
from typing import List


class Solution:
    # 유클리드 거리의 우선순위 큐(heap) 순서
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))

        return result