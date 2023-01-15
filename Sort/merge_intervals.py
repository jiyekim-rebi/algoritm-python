# 구간 병합
# httpd://leetcode.com/problems/merge-intervals
from typing import List


class Solution:
    # 1. 정렬 후 병합
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,   # List[List[int]]

        return merged