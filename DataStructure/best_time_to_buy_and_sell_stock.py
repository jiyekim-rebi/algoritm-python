# 주식을 사고팔기 가장 좋은 시점
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
import sys
from typing import List


class Solution:

    # 브루스 포트로 해봄 (n^2)
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    # 저점과 현재 값과의 차이 계산
    def maxProfit(self, prices: List[int]) -> int:
        # None 으로 잡으면 타입에러 발생할 수 있음
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit

