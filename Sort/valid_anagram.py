# 유효한 애너그램
# https://leetcode.com/problems/valid-anagram

class Solution:
    # 정렬
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)