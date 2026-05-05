class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        begin_counter = 0

        while begin_counter < len(prices):
            sliding_counter = begin_counter + 1
            while sliding_counter < len(prices):
                profit =  prices[sliding_counter] - prices[begin_counter]
                if profit > max_profit:
                    max_profit = profit
                sliding_counter += 1
            begin_counter += 1

        return max_profit
        