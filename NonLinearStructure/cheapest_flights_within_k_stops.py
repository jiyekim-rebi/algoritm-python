# K 경유지 내 가장 저렴한 항공권
# https://leetcode.com/problems/cheapest-flights-within-k-stops
import collections
import heapq
from typing import List


class Solution:
    # 다익스트라 알고리즘 응용버전
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(nil)

        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수 : 가격, 정점, 남은 가능 경유지 수
        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0: # 경유지 수가 0이 아닐때만 계산
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))

        return -1
