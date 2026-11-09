class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for elt in prices:
            maxP = max(maxP, elt - minBuy)
            minBuy = min(minBuy, elt)
        
        return maxP