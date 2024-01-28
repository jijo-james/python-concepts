class Solution:

    def max_profit(self, price_list: list[int]) -> int :
        buy, sell = 0, 1
        max_profit = 0
        list_count = len(price_list)

        while sell < list_count:
            if buy < sell:
                profit = price_list[sell] - price_list[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1

        return max_profit


s = Solution()

print(s.max_profit([7,1,5,3,6,4]))
