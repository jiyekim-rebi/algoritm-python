# B4: 셔틀버스
from datetime import time
from typing import List


def solution(n: int, t: int, m: int, timetable: List[str]) -> str:
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()

    current = 540
    for _ in range(n):
        for _ in range(m):
            # 대기가 있다면 1분전 도착
            if timetable and timetable[0] < current:
                candidate = timetable.pop(0) - 1
            else:
                candidate = current

        current += t

    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)