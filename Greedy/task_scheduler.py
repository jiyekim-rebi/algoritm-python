# 테스크 스케쥴러
# https://leetcode.com/problems/task-scheduler
import collections
from typing import List


class Solution:
    # 우선순위 큐
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n + 1): # 가장 개수 많은 아이템부터 출력 : 최대 힙
                sub_count += 1
                result += 1

                counter.subtract(task) # pop으로 추출되는건 아니라서 subtrack을 지정해서 한개씩 줄여나감
                # 0 이하인 아이템을 목록에서 완전히 제거처리함
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result