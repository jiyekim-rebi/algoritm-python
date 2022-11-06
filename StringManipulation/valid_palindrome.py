#유효한 팰린드롬(앞뒤가 똑같은 문장)
#https://leetcode.com/problems/valid-palindrome/

import collections
import re
from typing import Deque

#단순하게 리스트로 해결하기
def is_palindrome_list(s) -> bool:
    strs=[]
    for char in s:
        if char.isalnum(): #숫자, 영문 판별
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): #앞부분과 뒷부분의 결과를 매칭해감
            return False
    return True

#데크 자료형으로 풀어보기
def is_palindrome_deque(s) -> bool:
    # 자료형 데크 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

#슬라이싱
def is_palindrome_slicing(s) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::1]


if __name__=="__main__":
    temp = "abba"
    print("isPalindrome[list] : ", is_palindrome_list(temp))
    print("isPalindrome[deque] : ", is_palindrome_deque(temp))
    print("isPalindrome[slicing] : ", is_palindrome_slicing(temp))