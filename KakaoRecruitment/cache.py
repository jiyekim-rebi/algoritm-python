# B3: 캐시
import collections
from typing import List


# 입력 데이터: 캐시크기, 도시이름 배열
# 캐시사이즈: 0에서 30 이하
# 도시이름 배열: 도시 이름으로 된 문자열 배열, 최대 10만개
# 도시 이름당 최대 20자, 공백/숫자/특수문자 등이 없는 영문자로만 구성됨, 대소문자 구분 하지 않음.

# LRU(Least Recently Used): 가장 오래전에 사용한 아이템을 버리는 방식
def solution(cacheSize: int, cities: List[str]) -> int:
    elapsed: int = 0
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()

        # 캐시 히트 시 재삽입 처리
        if c in cache:
            cache.remove(c)
            cache.append(c)
            elapsed += 1
        else:
            cache.append(c)
            elapsed += 5

    return elapsed