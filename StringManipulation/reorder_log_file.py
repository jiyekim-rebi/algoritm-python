#로그파일 재정렬
#https://reetcode.com/problems/reorder-data-in-log-files
from typing import List

class Solution:
    # 람다, + 연산자 사용
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        # 람다 표현식을 사용하지 않는다면 아래와 같은 코드 사용
        # def func(x):
        #   return x.split()[1], x.split()[0]
        # s.sort(key=func)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits