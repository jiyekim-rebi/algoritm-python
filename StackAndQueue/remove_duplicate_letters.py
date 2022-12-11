# 중복 문자 제거
# https://leetcode.com/problems/remove-duplicate-letters
import collections


class Solution:
    # 재귀를 이용한 분리
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char)]
            # 전체 집합과 접미사 집합이 일치할때 분리처리함
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))

        return ''

    # 스택을 이용한 문자제거: 중복제거
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 문자가 남아있으면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
