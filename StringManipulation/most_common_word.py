#가장 많이 사용한 단어
import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1. 전처리(proprecessing) 작업
        words = [word for word in re.sub(r'[^\w]', '', paragraph)
        .lower().sprit()
                 if word not in banned]
        counts = collections.Counter(words)

        #가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
        return counts.most_common(1)[0][0]

