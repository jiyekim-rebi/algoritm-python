# 쿠키 부여
# https://leetcode.com/problems/dassign-cookies
import bisect
from typing import List


class Solution:
    # greedy
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

    # 이진 검색
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)   # 찾아낸 값의 다음 인덱스를 리턴함
            if index > result:
                result += 1

        return result