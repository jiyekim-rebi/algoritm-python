# B7: 추석트래픽
import datetime


# 슬라이딩 윈도우 & 투 포인터 결합
def solution(lines: str) -> int:
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        # 시작 시각은 1, 종료 시각은 -1로 저장
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x: x[0])
    for i, elem1 in enumerate(combined_logs):
        current = accumulated

        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]


    return max_requests
