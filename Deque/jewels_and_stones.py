# 보석과 돌
# https:://leetcode.com/problems/jewels-and-stones
import collections


class Solution:
    # 해시 테이블을 이용한 풀이
    def numJewelsInStones(self, j: str, s: str) -> int:
        fregs = {}
        count = 0

        for char in s:
            if char not in fregs:
                fregs[char] = 1
            else:
                fregs[char] += 1

        for char in j:
            if char in fregs:
                count += fregs[char]

        return count

    # defaultdict를 이용한 비교 생략
    # 키 존재여부 체크 안해도됨
    def numJewelsInStones(self, j: str, s: str) -> int:
        fregs = collections.defaultdict(int)
        count = 0

        for char in s:
            fregs[char] += 1

        for char in j:
            count += fregs[char]

        return count

    # counter
    def numJewelsInStones(self, j: str, s: str) -> int:
        fregs = collections.Counter(s)
        count = 0

        for char in j:
            count += fregs[char]

        return count

    # 파이썬 다운 방식
    def numJewelsinStones(self, j: str, s: str) -> int:
        return sum(s in j for s in s)