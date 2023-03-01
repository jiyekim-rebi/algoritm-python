# B1: 비밀지도
from typing import List

# 지도 둘 중 하나라도 벽이면 벽, 둘다 공백이면 공백 == OR 연산
def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    maps = []

    for i in range(n):
        maps.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))

    return maps