# 상위 K 빈도 요소
# https://leetcode.com/problems/top-k-frequent-elements
import collections
import heapq
from typing import List


class Solution:
    # counter를 이용한 음수 순 추출
    # 해시 테이블을 만들고 빈도수 저장, 우선순위 큐를 이용해 k번 이상 등장한 요소 찾아냄
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fregs = collections.Counter(nums)
        fregs_heap = []

        # 힙에 음수로 삽입
        for f in fregs:
            heapq.heappush(fregs_heap, (-fregs[f], f))

        topk = list()

        for _ in range(k):
            topk.append(heapq.heappop(fregs_heap)[1])

        return topk

    # 파이썬 다운 방식: most_common
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]