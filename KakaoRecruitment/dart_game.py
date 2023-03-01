# B2: 다트게임

# 기회는 3번
# 0 ~ 10점 사이
# Single: S(^1), Double: D(^2), Triple: T(^3)
# * = ^2, # = ^-1
# *와 #은 중첩될 수 있음(2개면 x2), 둘중 하나만 있거나 둘다 없음

def solution(dartResult: str) -> int:
    nums = [0]

    for s in dartResult:
        if s == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            # 이전 데이터 전부 두배처리
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= 1
        else:
            nums[-1] = nums[-1] * 10 + int(s)

    return sum(nums)