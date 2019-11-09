class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) == 0):
            return 0
        profits = [0]*len(prices)
        profits[0] = 0
        min_p = prices[0]
        for i in range(1,len(prices)):
            profits[i] = max(profits[i-1],prices[i]-min_p)
            if(prices[i]<min_p):
                min_p = prices[i]
                
        return profits[-1]
