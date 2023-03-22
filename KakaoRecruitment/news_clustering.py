# B5: 뉴스 클러스터링
# 자카드 유사도
import collections
from typing import re


def solution(str1: str, str2: str) -> int:
    str1s = [
        str1[i:i + 2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i:i + 2].lower())
    ]
    str2s = [
        str2[i:i + 2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i + 2].lower())
    ]

    # 교집합
    intersection = sum((collections.Counter(str1s) & collections.Counter(str2s)).values())

    # 합집합
    union = sum((collections.Counter(str1s) | collections.Counter(str2s)).values())

    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)
