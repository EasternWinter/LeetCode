class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fBuy = -prices[0]
        fSell = 0
        sBuy = -prices[0]
        sSell = 0
        for price in prices[1:]:
            fBuy = max(fBuy, -price)
            fSell = max(fSell, fBuy + price)
            sBuy = max(sBuy, fSell - price)
            sSell = max(sSell, sBuy + price)
        return sSell