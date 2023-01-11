# 배열의 k번째 큰 요소
# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import List


# Ref. 상위 K 빈도 요소
class Solution:
    # 1. heapq module
    # 음수로 저장한 다음 가장 낮은 수 부터 추출해서 부호를 변환시킴
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

    # 2. heapq - heapify
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    # 3. heapq - nlargest
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # n번째 큰값 추출
        return heapq.nlargest(k, nums)[-1]

    # 4. 정렬을 이용한 풀이
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

